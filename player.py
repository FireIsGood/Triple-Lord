stats = {
  "name": "defaultName",
  "level": 1,
  "gold": 0,
  "max_hp": 20,
  "max_sp": 10,
  "max_mp": 0,
  "atk": 10,
  "def": 5,
  "mag": 0,
  "hp": 20,
  "sp": 10,
  "mp": 0,
}

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