def nameclr(input):
  return f"\033[96m{input}\033[0m"

menu_color = 34
def menuclr(input):
  return f"\033[{menu_color};4m{input}\033[0m"

def red(input):
  return f"\033[91m{input}\033[0m"

def green(input):
  return f"\033[92m{input}\033[0m"

def blue(input):
  return f"\033[94m{input}\033[0m"

def yellow(input):
  return f"\033[33m{input}\033[0m"
