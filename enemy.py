from colors import red 

# Most is self explanatory, but atk and def are special
# Atk is chosen at random if attacking from list
# First term in def is passive defense second is active
# Atk lines correspond to damage values

stats = {
  "hedge_peon": {
    "name": red("Hedge Peon"),
    "level": 1,
    "locations": ["forest"],
    "art": '''
       ..::::.
     ::::::::::
    /o    !::::
   *---u--u---
    ''',
    "max_hp": 35,
    "atk": [6, 8, 10],
    "atk_line": [f"{red('Hedge Peon')} accidentally bumps into you.", f"{red('Hedge Peon')} rolls at you agressively!", f"{red('Hedge Peon')} does a backflip and lands on you!"],
    "def": [1, 10],
    "def_line": f"{red('Hedge Peon')} rolls up.",
    "hp": 35,
  },
  
    "bad_flower": {
    "name": red("Bad Flower"),
    "level": 1,
    "locations": ["forest"],
    "art": '''
     /^^\  
     \/\/    ,---.
     \||    /('==-0
      ||/  //
    ''',
    "max_hp": 25,
    "atk": [7, 10, 14],
    "atk_line": [f"{red('Bad Flower')} fires wildly, missing most of the shots.", f"{red('Bad Flower')} does a spin and barely hits.", f"{red('Bad Flower')} aims in and fires!"],
    "def": [0, 8],
    "def_line": f"{red('Bad Flower')} ducks for cover.",
    "hp": 25,
  },
  
}

