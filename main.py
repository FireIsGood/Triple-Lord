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

def clear():
  print("\033[H\033[J",end="")

def main():
  error = False
  while True:
    print(f"\033[31;40;1m{art.top_bar}")
    print(f"{art.logo}\033[0m")
    print("\033[93ma game by FireIsGood                                    \033[33mtype 'main()' if the game crashes\033[0m\n")
    print(f'                       {green("N")}ew Game           {green("L")}oad Game           {green("S")}ettings\n')
    if error == True:
      print("Error, try again.")
    selection = input().lower()
    if selection in ("n", "new", "new game"):
      clear()
      print("New game!")
      character_creator()
      selection = input().lower()
    elif selection in ("l", "load", "load game"):
      clear()
      print("Load game!")
      selection = input().lower()
    elif selection in ("s", "settings"):
      clear()
      print("Settings!")
      selection = input().lower()
    else:
      clear()
      error = True

def character_creator():
  print("Welcome to the world of Triple Lord.")
  print("What is your name?")
  input("\0")


      
# Start Game
main()