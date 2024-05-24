import random
import sys

JAPANESE_NUMBERS: dict = {
    1: 'ICHI', 2: 'NI',
    3: 'SAN', 4: 'SHI',
    5: 'GO', 6: 'ROKU',
}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

purse:int  = 5000

while True:
    # Place your bet:
    print(f"You have {purse} mon. How much do you bet? (or QUIT)")
    while True:
        pot = input("> ")
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            # This is a valid bet.
            pot = int(pot) 
            break

    # Roll the dice.
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams th e cup on the floor, still covering the")
    print("dice and asks for your bet.")
    print()
    print("     CHO (even) or HAN (odd)?")

    # Let the player bet cho or han:
    while True:
        bet = input("> ").upper()
        if bet != "CHO" and bet != "HAN":
            print("Please enter either 'CHO' or 'HAN'.")
            continue
        else:
            break

    # Reveal the dice results:
    print("The dealer lifts the cup to reveal:")
    print(f"  {JAPANESE_NUMBERS[dice1]} - {JAPANESE_NUMBERS[dice2]}")
    print(f"    {dice1} - {dice2}")

    # Determin if the player won:
    roll_is_even: bool = (dice1 + dice2) % 2 == 0

    correct_bet: str = ""
    if roll_is_even:
        correct_bet = "CHO"
    else:
        correct_bet = "HAN"

    player_won: bool = bet == correct_bet

    # Display the bet results:
    if player_won:
        print(f"You won! You take {pot}mon.")
        purse = purse + pot 
        print(f"The house collects a {pot//10}mon fee.")
        purse = purse - (pot//10)
    else:
        purse = purse - pot 
        print("You lost!")

    # Check if the player has run out of money:
    if purse == 0:
        print("You have run out of money")
        print("Thanks for playing!")
        sys.exit()


