from misc import pause
from colors import green
import math

stats = {
  "name": "defaultName",
  "level": 1,
  "exp": 0,
  "gold": 0,
  "max_hp": 20,
  "max_sp": 10,
  "max_mp": 0,
  "hp": 20,
  "sp": 10,
  "mp": 0,
  
  "base_atk": 5,
  "base_def": 0,
  "base_mag": 0,
  "atk": 0,
  "def": 0,
  "mag": 0,

  "equip_weapon": "stick",
  "equip_body": "boots",
  "equip_code": "",
}

inventory = {
  "stick": 1,
  "boots": 1,
  "gun": 1,
}

equipment_dictionary = {
  "": {
    "name": "",
    "description": "Nothing.",
    "atk": 0,
    "def": 0,
    "mag": 0,
  },
  "stick": {
    "name": green("Stick"),
    "description": "It emits a faint warmth.\n+5 Attack",
    "slot": "equip_weapon",
    "atk": 5,
    "def": 0,
    "mag": 0,
  },
  "gun": {
    "name": green("Gun"),
    "description": "Dev tool\n+500 Attack",
    "slot": "equip_weapon",
    "atk": 500,
    "def": 0,
    "mag": 0,
  },
  "boots": {
    "name": green("Boots"),
    "description": "Your shoes. You feel stylish!\n+5 Defense",
    "slot": "equip_body",
    "atk": 0,
    "def": 5,
    "mag": 0,
  },
}

equip_types = ["equip_weapon", "equip_body", "equip_code"]
equip_types_clean = {
  "equip_weapon": [f"{green('W')}eapon", "weapon", "w"],
  "equip_body": [f"{green('B')}ody", "body", "b"],
  "equip_code": [f"{green('C')}ode", "code", "c"],
}

def statboost_calc(stat):
  statboost = 0
  for item in equip_types:
    statboost += equipment_dictionary[stats[item]][stat]
  return statboost

def recalculate():
  '''Recalculates stats based on base and equipment and level based on exp'''
  # Level stats at 1 for 0-5 exp, then costs 5*2^[level-1] exp to obtain
  # so basically start at 5 and double the total exp needed every level
  if stats["exp"] < 5:
    stats["level"] = 1
  else: # do funky calc to find level
    stats["level"] = math.floor(math.log((2 / 5) * stats["exp"])/math.log(2)+1)
  # Stats are base plus level for max hp, max sp, and base atk/def past level 1
  stats["max_hp"] = 20 + stats["level"] - 1
  stats["max_sp"] = 10 + stats["level"] - 1
  stats["base_atk"] = 5 + stats["level"] - 1
  stats["base_def"] = 0 + stats["level"] - 1
  
  
  stats["atk"] = max(stats["base_atk"] + statboost_calc("atk"),0)
  stats["def"] = max(stats["base_def"] + statboost_calc("def"),0)
  stats["mag"] = max(stats["base_mag"] + statboost_calc("mag"),0)

def print_equip_types():
  for item in equip_types:
    green(print(equip_types_clean[item][0]))

def print_items_from_slot(slot):
  for item in inventory:
    if equipment_dictionary[item]["slot"] == slot:
      print(coolname(item))

def equip(item):
  if item in inventory:
    name = coolname(item)
    item_slot = equipment_dictionary[item]["slot"]
    slot_name = equip_types_clean[equipment_dictionary[item]["slot"]][0]
    stats[item_slot] = item
    print(f"You equip {name} to your {slot_name}")
  else:
    print(f"You do not have {item}")
    pause()

def unequip(slot):
  if slot in equip_types:
    stats[slot] = ""
  else:
    print(f"{slot} is not a equipment slot")
    return "error"
    pause()

def inspect(item):
  if item in inventory:
    name = coolname(item)
    description = equipment_dictionary[item]["description"]
    slot = equip_types_clean[equipment_dictionary[item]["slot"]][0]
    print(f'''
{name}
{description}
\033[93m{slot}\033[0m\
''')
    pause()
  else:
    print(f"{item} is not in your inventory")
    pause()

def coolname(item):
  return equipment_dictionary[item]["name"]

def from_nick(input):
  '''From an input of one of the slot names, returns the technical name.'''
  for key in equip_types_clean:
    if input in equip_types_clean[key]:
      return key
      

def refresh():
  stats["hp"] = stats["max_hp"]
  stats["sp"] = stats["max_sp"]
  stats["mp"] = stats["max_mp"]

def damage(hit):
  '''Damages the player for a positive value'''
  stats["hp"] = max(stats["hp"] - hit, 0)

def stamina(hit):
  '''Modifies stamina. \n
  Use positive to add and negative to subtract'''
  stats["sp"] = min(max(stats["sp"] + hit, 0),stats["max_sp"])