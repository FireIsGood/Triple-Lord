# An rpg game!
# Character has:
#  perma stats [Def] [Atk] [Mag]
#  variable stats [Hp] [Sp] [Mp] and [Gold]
# Stats based on equipment and level
# Level up based on exp from defeating enemies, small benefit
# Buy gear from shops, large benefit
# Win lord contracts from fighting bosses, pick one type
# Fight enemies!
#  damage is atk - def
#  use stamina per attack with diff taking more
#  health restores available at town
#  or use potions between combat
# Magic system
#  cast spells out of combat to buff self temporarily
#  mana restores at town
#  or use potions between combat
# DEFEAT THE TRIPLE LORD
# todo: make the game
import random
import art
from colors import red, blue, green, yellow, nameclr, menuclr, menu_color
from misc import pause, clear
import player
import enemy

location = "world_map"


  

def location_nick(input):
  '''Finds the location via list of nicknames'''
  for l_key, l_properties in art.places.items():
    for property in l_properties:               # Searching properties
      if property == "names":                   # Finds property "names"
        nicknames = art.places[l_key][property] # Pulls the list of nicknames
        if input in nicknames:                  # Checks if the input is a valid nickname
          return l_key                          # Returns the location's true name

def enemy_list(input):
  '''Creates a list of enemies in a location'''
  enemy_pool = []
  for e_name, e_properties in enemy.stats.items():
    for property in e_properties:
      if property == "locations":
        locations = enemy.stats[e_name][property]
        if input in locations:
          enemy_pool.append(e_name)
  return enemy_pool
  
def character_creator():
  '''Character creation script. Loads on New Game'''
  print("Welcome to Triple Lord.")
  player.stats["name"] = input('What is your name? \033[96m')
  print("\033[0m",end="")
  print(f"{nameclr(player.stats['name'])}? What a wonderful name!")
  
  if "Malkuth" in player.stats['name']:
    print("\033[95mDebug Mode Activated\033[0m")
    # debug = True

  print(f'''
Type {menuclr("T")} to travel or {menuclr("S")} to look at your stats.
Many places can be shortened to the first letter.
If your hp drops to 0, you die!
Good luck!
        ''')
  pause()
  game()
  
def menu_action():
  print(f'{menuclr("T")}ravel {menuclr("S")}tats  ',end="")
  # Extra prompts if on an adventure
  if game_mode == "adventure":
    print(f'|  {menuclr("A")}dventure',end="")

  # Menu input and parsing
  menu_input = input(f"\n\033[{menu_color}m").lower()
  print("\033[0m",end="")
  if menu_input in ["t", "travel"]:
    travel()
  elif menu_input in ["s", "stats"]:
    stats_menu()
  elif menu_input in ["a", "adventure"] and game_mode == "adventure":
    if player.stats["hp"] > 0:
      adventure()
    else:
      print("You are too badly hurt to adventure! Rest at an inn.")
      pause()
  else:
    if menu_input == "":
      print(f"Please type a menu input")
    else:
      print(f"{menu_input} is not a valid menu input")
    pause()

def travel():
  global location
  global travel_error
  travel_input = input("Walk to: \033[92m").lower()
  travel_location = location_nick(travel_input)
  print("\033[0m",end="")
  if travel_location in art.places[location]["connections"]:
    print(f'You went to {art.places[travel_location]["display_name"]}.')
    location = travel_location
    pause()
  else:
    print(f"You cannot go to {travel_input.title()} from here.")
    pause()
    
def stats():
  print(f'''\
{nameclr(player.stats["name"])} {yellow(str(player.stats["gold"]) + " Gold")} 
Hp: {player.stats["hp"]}/{player.stats["max_hp"]}
Sp: {player.stats["sp"]}/{player.stats["max_sp"]}
Mp: {player.stats["mp"]}/{player.stats["max_mp"]}\
''')
  
def stats_menu():
  player.recalculate()
  exit_menu = False
  while exit_menu == False:
    clear()
    print(art.bar)
    stats()
    print(f'''
\033[1mStats:\033[0m
Atk: {player.stats["atk"]} ({player.stats["base_atk"]})
Def: {player.stats["def"]} ({player.stats["base_def"]})
Mag: {player.stats["mag"]} ({player.stats["base_mag"]})
          
\033[1mEquipment:\033[0m
Body:   {player.coolname(player.stats["equip_body"])}
Weapon: {player.coolname(player.stats["equip_weapon"])}
Code:   {player.coolname(player.stats["equip_code"])}
''')
    print(art.bar)
  
    def print_equip_types():
      for item in player.equip_types:
        green(print(item))
    
    print(f'{menuclr("C")}lose Menu  {menuclr("E")}quip  {menuclr("U")}nequip  {menuclr("I")}nspect',end="")
    stats_input = input(f"\n\033[{menu_color}m").lower()
    print("\033[0m",end="")
    
    # equip an item to a slot
    if stats_input in ["e", "equip"]:
      print_equip_types()
      equip_item = input("Equip which slot? ")
      player.equip(equip_item)

    # Unequip an item from a slot
    elif stats_input in ["u", "unequip"]:
      print_equip_types()
      unequip_item = input("Unequip which slot? ")
      player.unequip(unequip_item)
      
    # Inspect an item in the inventory
    elif stats_input in ["i", "inspect"]:
      print("Inventory:")
      for item in player.inventory:
        print(player.coolname(item))
      inspect_item = input("Inspect what item? \033[92m")
      print("\033[0m",end="")
      player.inspect(inspect_item)
      pause()
    
    # Close menu
    elif stats_input in ["c", "close", "close menu"]:
      exit_menu = True
    
    else:
      if stats_input == "":
        print(f"Please type a menu input")
      else:
        print(f"{stats_input} is not a valid menu input")
      pause()
    
    player.recalculate()

def adventure():
  global location
  if random.randint(1,100) <= art.places[location]["battle_chance"]:
    random_enemy = random.choice(enemy_list("forest"))
    battle(random_enemy)
  else:
    print("You adventure and find nothing!")
    pause()
  
  
def battle(name):
  battle_finished = False
  current_enemy = enemy.stats[name]
  while battle_finished == False:
    player_temp_defense = 0
    
    # Decide Enemy action
    enemy_action = random.choice(["atk", "def"])
    if enemy_action == "atk":
      enemy_intention = red("Attack")
      current_enemy_attack_id = random.randint(0, len(current_enemy["atk"])-1)
      current_enemy_attack = current_enemy["atk"][current_enemy_attack_id]
      current_enemy_defense = current_enemy["def"][0]
    elif enemy_action == "def":
      enemy_intention = blue("Defend")
      current_enemy_attack = 0
      current_enemy_defense = current_enemy["def"][1]

    # Player turn
    player_has_acted = False
    while player_has_acted == False:
      # Draw UI
      clear()
      print(art.bar)
      print(f'You encounter {current_enemy["name"]}!!')
      print(current_enemy["art"])
      print(f'Hp: {current_enemy["hp"]}/{current_enemy["max_hp"]}')
      
      enemy_prediction = f'{current_enemy["name"]} is going to {enemy_intention}'
      if "Attack" in enemy_intention:
        predicted_damage = current_enemy_attack - player_stats["def"]
        enemy_prediction += f" for {current_enemy_attack} damage, dealing {predicted_damage} damage"
      print(enemy_prediction)
      
      print(art.bar)
      stats()
  
      # Get player input
      print(f'{menuclr("A")}ttack {menuclr("D")}efend  {menuclr("R")}un',end="")
      battle_input = input(f"\n\033[{menu_color}m").lower()
      print("\033[0m",end="")
  
      # Attack Command
      if battle_input == "a":
        if player.stats["sp"] > 0:
          player.stamina(-1)
          if enemy_action == "def": # Print enemy defensive line
            print(current_enemy["def_line"])
          player_has_acted = True
          player_damage_final = max(player.stats["atk"] - current_enemy_defense, 1) # Player minimum 1 damage
          print(f"You attack, dealing {player_damage_final} damage!")
          current_enemy["hp"] = current_enemy["hp"] - player_damage_final
          if current_enemy["hp"] <= 0:
            battle_finished = True
            print(f"\033[1mYou defeated {current_enemy['name']}\033[0m")
        else:
          print("You are too tired to attack.")
  
      # Defend command
      elif battle_input == "d":
        player.stamina(+1)
        player_has_acted = True
        player_temp_defense = player.stats["def"] + 1
        print(f'You block, temporarily increasing your defense to {player.stats["def"] + player_temp_defense}')
  
      # Run command
      elif battle_input == "r":
        player_has_acted = True
        if current_enemy["level"] <= player.stats["level"]:
          print("Escaped successfully!")
          battle_finished = True
        elif random.randint(0,1) == 1:
          print("Escaped successfully!")
          battle_finished = True
        else:
          print("Couldn't escape!")
          
      # Catch bad inputs
      else:
        if battle_input == "":
          print(f"Please type a battle command")
        else:
          print(f"{battle_input} is not a valid battle command")
        pause()
    
    # Resolve enemy damage
    if battle_finished == False:
      if enemy_action == "atk":
        damage_player_final = max(current_enemy_attack - (player.stats["def"] + player_temp_defense), 0)
        if damage_player_final > 0:
          print(f'{current_enemy["atk_line"][current_enemy_attack_id]}')
          print(f"You took {red(damage_player_final)} damage!")
          player.damage(damage_player_final)
          if player.stats["hp"] <= 0:
            battle_finished == True
            print("You were defeated!")
        else:
          print(f'{current_enemy["name"]} bounced off harmlessly!')
      pause()
    
  pause()

  
# Main game logic
# This is the main menu
def main():
  '''Opens the Main Menu'''
  error = False
  while True:
    
    clear()
    print(f"{art.bar_title}")
    print(f"{art.logo}\033[0m")
    print(f"{art.bar_title}")
    print("\033[93ma game by FireIsGood                                    \033[33mtype 'main()' if the game crashes\033[0m\n")
    print(f'                       {menuclr("N")}ew Game           {menuclr("L")}oad Game           {menuclr("S")}ettings\n')
    
    if error == True:
      print("Error, try again.")
    selection = input().lower()
    if selection in ("n", "new", "new game"):
      clear()
      character_creator()
    elif selection in ("l", "load", "load game"):
      clear()
      game()
    elif selection in ("s", "settings"):
      clear()
      print("Settings!")
      selection = input().lower()
    else:
      error = True


def game():
  '''Game State. Draws the art for travel and adventure modes'''
  global location
  global game_mode
  while True: # Loop meny actions
    clear()
    print(art.bar)
    print(art.places[location]["art"])
    print(art.bar)
    stats()
    
    # Menu logic
    game_mode = art.places[location]["mode"]
    if game_mode == "travel":
      menu_action()
    elif game_mode == "adventure":
      menu_action()



# Start Game
main()