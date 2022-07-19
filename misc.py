def clear():
  '''Clears the screen'''
  print("\033[H\033[J",end="")

def pause():
  input("\033[90m<press enter to continue>\033[0m")