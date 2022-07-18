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
from colors import green
import player

location = "world_map"

def clear():
  '''Clears the screen'''
  print("\033[H\033[J",end="")

def pause():
  input("\033[90m<press enter to continue>\033[0m")

def location_nick(input):
  '''Finds the location via list of nicknames'''
  for l_key, l_properties in art.places.items():
    for property in l_properties:
      if property == "names":
        nicknames = art.places[l_key][property]
        if input in nicknames:
          return l_key

def main():
  '''Main menu'''
  error = False
  while True:
    clear()
    print(f"\033[31;40;1m{art.top_bar}")
    print(f"{art.logo}\033[0m")
    print("\033[93ma game by FireIsGood                                    \033[33mtype 'main()' if the game crashes\033[0m\n")
    print(f'                       {green("New Game           Load Game           Settings")}\n')
    if error == True:
      print("Error, try again.")
    selection = input().lower()
    if selection in ("n", "new", "new game"):
      clear()
      character_creator()
    elif selection in ("l", "load", "load game"):
      clear()
      map()
    elif selection in ("s", "settings"):
      clear()
      print("Settings!")
      selection = input().lower()
    else:
      error = True

def character_creator():
  '''Character creation script. Loads on New Game'''
  print("Welcome to the world of Triple Lord.")
  player.player["name"] = "\033[96m" + input('What is your name? \033[96m') + "\033[0m"
  print("\033[0m",end="")
  print(f"{player.player['name']}? That's a good name.")
  if "Malkuth" in player.player['name']:
    print("\033[95mDebug Mode Activated\033[0m")
    # debug = True
  map()

def map():
  '''map state'''
  global location
  error = False
  travel_input = ""
  while True:
    clear()
    print(art.top_bar)
    print(art.places[location]["art"])
    if error == True:
      print(f"You cannot go to {travel_input.title()} from here.")
    
    # Travel logic
    if art.places[location]["mode"] == "travel":
      travel_input = input().lower()
      travel_location = location_nick(travel_input)
      if travel_location in art.places[location]["connections"]:
        print(f"You went to the {travel_input.title()}.")
        location = travel_location
        error = False
        pause()
      else:
        error = True

# Start Game
main()