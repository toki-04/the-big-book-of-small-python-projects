import random

print("""Carrot in a Box, by Al Sweigart al@inventwithpython.com

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then 
gets to decide if they want to swap boxes or not.
""")

input("Press Enter to begin...")

p1_name: str = input("Human player 1, enter your name: ")
p2_name: str = input("Human player 2, enter your name: ")
player_names = p1_name[:11].center(11) + "     " + p2_name[:11].center(11)

print('''HERE ARE TWO BOXES:
  __________      __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   RED   | |   |   GOLD  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/''')

print()
print(player_names)
print()
print(p1_name + ", you have a RED box in front of you.")
print(p2_name + ", you have a GOLD box in front of you.")
print()
print(p1_name + ", you will get to look into your box.")
print(p2_name.upper() + ", close your eyes and don't look!!!")
input("When "+p2_name+" has closed their eyes, press Enter...")
print()

print(p1_name + " here is the inside of your box:")

carrot_in_first_box: bool = False 
if random.randint(1, 2) == 1:
    carrot_in_first_box = True

if carrot_in_first_box:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|     __________
 /    ||   /|    /         /|
+---------+ |   +---------+ |
|   RED   | |   |   GOLD  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/
(carrot!)''')
    print(player_names)
else:
    print('''
   _________
  |         |
  |         |
  |_________|     __________
 /         /|    /         /|
+---------+ |   +---------+ |
|   RED   | |   |   GOLD  | |
|   BOX   | /   |   BOX   | /
+---------+/    +---------+/
(no carrot!)''')
    print(player_names)
    
input("Press Enter to continue...")

print("\n" * 100) # Clear the screen by printing several newlines.
print(p1_name + ', tell ' + p2_name + ' to open their eyes.')
input("Press Enter to continue")

print()
print(p1_name + ", say one of the following sentences to " + p2_name + '.')
print("  1) There is a carrot in my box.")
print("  2) There is not a carrot in my box.")
print()
input("Then press Enter to continue...")

print()
print(p2_name + ", do you want to swap boxes with " + p2_name + "? YES/NO")
while True:
    response: str = input("> ").upper()
    if not (response.startswith("Y") or response.startswith("N")):
        print(p2_name + ", please enter 'YES' or 'NO'")
    else:
        break


first_box: str = "RED " # Note the space after the "D".
second_box: str = "GOLD"

if response.startswith("Y"):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box

print('''HERE ARE THE TWO BOXES:
   __________      __________
  /         /|    /         /|
 +---------+ |   +---------+ |
 |   {}  | |   |   {}  | |
 |   BOX   | /   |   BOX   | /
 +---------+/    +---------+/'''.format(first_box, second_box))
print(player_names)

input("Press Enter to reveal the winner...")
print()

if carrot_in_first_box:
    print('''
    ___VV____
   |   VV    |
   |   VV    |
   |___||____|      __________
  /    ||   /|    /         /|
 +---------+ |   +---------+ |
 |   {}  | |   |   {}  | |
 |   BOX   | /   |   BOX   | /
 +---------+/    +---------+/'''.format(first_box, second_box))
else:
    print('''
                    ___VV____
                   |   VV    |
                   |   VV    |   
   __________      |___||____|
  /         /|    /    ||   /|
 +---------+ |   +---------+ |
 |   {}  | |   |   {}  | |
 |   BOX   | /   |   BOX   | /
 +---------+/    +---------+/'''.format(first_box, second_box))

print(player_names)

# This modification made possible through the 'carrot_in_first_box' variable
if carrot_in_first_box:
    print(p1_name + ' is the winner!')
else:
    print(p2_name + ' is the winner!')

print("Thanks for playing!")




