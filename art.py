from colors import green

logo = '''                                                                                          
                     _______   _       _        _                   _                     
                    |__   __| (_)     | |      | |                 | |                    
                       | |_ __ _ _ __ | | ___  | |     ___  _ __ __| |                    
                       | | '__| | '_ \| |/ _ \ | |    / _ \| '__/ _` |                    
                       | | |  | | |_) | |  __/ | |___| (_) | | | (_| |                    
                       |_|_|  |_| .__/|_|\___| |______\___/|_|  \__,_|                    
                                | |                                                       
                                |_|                                                       
                                                                                          '''
top_bar = ">==-===-===-==<>==-===-===-==<>==-===-===-==<>==-===-===-==<>==-===-===-==<>==-===-===-==<"


places = {
  "world_map": {
    "names": ["map", "world map"],
    "art": f'''Where would you like to travel?
  
      _j  __                  
     /o \/o \      /\ /\      
     |# ||# |     /\\\ //\       _---._
      /o \        /\|\|/\      /##\ ' \.
      |# |       /||\ /||\    /####|  / \\
      {green("Town         Forest        Cave")}
    ''',
    "mode": "travel",
    "connections": ["town", "forest"],
  },
  "town": {
    "names": ["town", "gamer zone"],
    "art": f'''You can return to the {green("Map")}
The town is bustling.
                  h______
                 /  Inn  \\
          o      |    ._ |
         -+-     | [] |_||
         / \     | []    |
      Some {green("Nerd")}   The {green("Inn")}
    ''',
    "mode": "travel",
    "connections": ["world_map"],
  }
}