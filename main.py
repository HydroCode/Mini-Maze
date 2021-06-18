import os
from getch import getch
import cursor


def clear():
  os.system('clear')



map = [
  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'd', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'b'],
  ['b', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'e', 'b'],
  ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
]

def print_map():
  global i
  for x in map:
    out = ''
    for i in x:
      if i == 'p':
        out += ' '
      elif i == 'b':
        out += '░'
      elif i == 'u':
        out += '█'
      elif i == 'd':
         out += 'o'
      elif i == 'e':
        out +='■'
    print(out)

cursor.hide()

y = 1
x = 1

while True:
  os.system('clear')

  map[y][x] = 'u'
  
  print_map()

  try:
    map[y][x] = 'p'

    keyPressed = getch()

    if keyPressed == 's'and map[y+1][x] != 'b':
      y += 1

    elif keyPressed == 'w'and map[y-1][x] != 'b':
      y -= 1

    elif keyPressed == 'd'and map[y][x+1] != 'b':
      x += 1

    elif keyPressed == 'a'and map[y][x-1] != 'b':
      x -= 1

    if map[y][x] == 'd':
      clear()
      print("You lost...") 
      break

    if map[y][x] == 'e':
      os.system('clear')
      print("Victory is yours...")
      break
  except:
    pass 
  
  
