from misc import pause
from colors import green

stats = {
  "name": "defaultName",
  "level": 1,
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

  "equip_body": "",
  "equip_weapon": "stick",
  "equip_code": "",
}

inventory = {
  "stick": 1,
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
}

equip_types = ["equip_body", "equip_weapon", "equip_code"]
equip_types_clean = {
  "equip_body": "Body",
  "equip_weapon": "Weapon",
  "equip_code": "Code",
}

def statboost_calc(stat):
  statboost = 0
  for item in equip_types:
    statboost += equipment_dictionary[stats[item]][stat]
  return statboost

def recalculate():
  '''Recalculates stats based on base and equipment'''
  stats["atk"] = max(stats["base_atk"] + statboost_calc("atk"),0)
  stats["def"] = max(stats["base_def"] + statboost_calc("def"),0)
  stats["mag"] = max(stats["base_mag"] + statboost_calc("mag"),0)

def equip(item):
  if item in inventory:
    item_slot = equipment_dictionary[item]["slot"]
    stats[item_slot] = item
  else:
    print("You do not have this item")
    pause()

def unequip(slot):
  if slot in equip_types:
    stats[slot] = ""
  else:
    print(f"{slot} is not a equipment slot")
    pause()

def inspect(item):
  if item in inventory:
    name = coolname(item)
    description = equipment_dictionary[item]["description"]
    slot = equip_types_clean[equipment_dictionary[item]["slot"]]
    print(f'''
{name}
{description}
\033[93m{slot}\033[0m\
''')
  else:
    print(f"{item} is not in your inventory")
    pause()

def coolname(item):
  return equipment_dictionary[item]["name"]

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