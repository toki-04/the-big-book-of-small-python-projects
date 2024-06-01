import random
import sys

print('''Dice Roller, by Al Sweigart al@inventwithpython.com

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
    3d6 rolls three 6-sided dice
    1d10+2 rolls one 10-sided die, and adds 2
    2d38-1 rolls two 38-sided die, and subtracts 1
    QUIT quits the program
''')

while True:
    try:
        dice_str = input("> ")
        if dice_str.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        # Clean up the dice string:
        dice_str = dice_str.lower().replace(" ", "")

        # Find the "d" in the dice string input:
        d_index = dice_str.find("d")

        if dice_str == 1:
            raise Exception("Missing the 'd' character.")

        # Get the number of dice. (The "3" in "3d6+1"):
        number_of_dice = dice_str[:d_index]

        if not number_of_dice.isdecimal():
            raise Exception("Missing the number of dice.")

        number_of_dice = int(number_of_dice)

        # Find if there is a plus or minus sign for a modifier:
        mod_index = dice_str.find("+")
        if mod_index == -1:
            mod_index = dice_str.find("-")

        # Find the number of sides. (The "6" in "3d6+1"):
        if mod_index == -1:
            number_of_sides = dice_str[d_index + 1:]
        else:
            number_of_sides = dice_str[d_index + 1: mod_index]

        if not number_of_sides.isdecimal():
            raise ("Missing the number of sides.")
        number_of_sides = int(number_of_sides)

        # Find the modifier amount. (The "1" in "3de6+1"):
        if mod_index == -1:
            mod_amount = 0
        else:
            mod_amount = int(dice_str[mod_index + 1:])
            if dice_str[mod_index] == "-":
                # Change the modification amount to negative
                mod_amount = -mod_amount

        # Simulate the dice rolls:
        rolls = []
        for i in range(number_of_dice):
            roll_result = random.randint(1, number_of_sides)
            rolls.append(roll_result)

        # Display the total:
        print('Total:', sum(rolls) + mod_amount, '(Each die:', end='')

        # Display the individual rolls:
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(", ".join(rolls), end="")

        # Display the modifier amount:
        if mod_amount != 0:
            mod_sign = dice_str[mod_index]
            print(', {}{}'.format(mod_sign, abs(mod_amount)), end='')
        print(')')
    except Exception as exc:
        # Catch any exceptions and display the message to the user:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue  # Go back to the dice string prompt.
