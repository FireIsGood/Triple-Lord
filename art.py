from colors import green

bar = ">==-===-===-==<>==-===-===-==<>==-===-===-==<>==-===-===-==<>==-===-===-==<>==-===-===-==<\033[0m"
bar_title = f"\033[31;40m{bar}\033[0m"
logo = '''\033[31;40;1m                                                                                          
                     _______   _       _        _                   _                     
                    |__   __| (_)     | |      | |                 | |                    
                       | |_ __ _ _ __ | | ___  | |     ___  _ __ __| |                    
                       | | '__| | '_ \| |/ _ \ | |    / _ \| '__/ _` |                    
                       | | |  | | |_) | |  __/ | |___| (_) | | | (_| |                    
                       |_|_|  |_| .__/|_|\___| |______\___/|_|  \__,_|                    
                                | |                                                       
                                |_|                                                       
                                                                                          \033[0m'''



places = {
  "world_map": {
    "display_name": "The World Map",
    "names": ["map", "world map", "m"],
    "art": f'''Where would you like to travel?
  
      _j  __                  
     /o \/o \      /\ /\      
     |# ||# |     /\\\ //\       _---._
      /o \        /\|\|/\      /##\ ' \.
      |# |       /||\ /||\    /####|  / \\
      {green("T")}own         {green("F")}orest        {green("C")}ave")
    ''',
    "mode": "travel",
    "connections": ["town", "forest"],
  },
  
  "town": {
    "display_name": "The Town",
    "names": ["town", "gamer zone", "t"],
    "art": f'''You can return to the {green("M")}ap
The town is bustling.
                  h______
                 /  Inn  \\
          o      |    ._ |
         -+-     | [] |_||
         / \     | []    |
      Some {green("N")}erd   The {green("I")}nn
    ''',
    "mode": "travel",
    "connections": ["world_map"],
  },
  
  "forest": {
    "display_name": "The Forest",
  "names": ["forest", "weedy", "f"],
  "art": f'''You can return to the {green("M")}ap
You are in a Forest\033[32m
    
                                 ^ 
     ^  ^  ^           ^  ^   ^ /|\ ^  ^   ^ 
    /|\/|\/|\         /|\/|\ /|\/|\/|\/|\ /|\\
    /|\/|\/|\         /|\/|\ /|\/|\/|\/|\ /|\\
    uwwuwuwwwu\033[33m========\033[32mwuwwuuwuuuwuwuuuwuuwuuw\033[0m
    ''',
  "mode": "adventure",
  "connections": ["world_map"],
  "battle_chance": 30,
  },
}