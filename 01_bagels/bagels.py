"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python" https://nostarch.com/inventwithpython
Tags: short, game, puzzle"""

import os
from sys import platform
import random
from termcolor import colored
from tabulate import tabulate

NUM_DIGITS = 3
MAX_GUESSES = 10

table = []
headers = ["#", "GUESS", "CLUE"]

title = """

██████╗░░█████╗░░██████╗░███████╗██╗░░░░░░██████╗
██╔══██╗██╔══██╗██╔════╝░██╔════╝██║░░░░░██╔════╝
██████╦╝███████║██║░░██╗░█████╗░░██║░░░░░╚█████╗░
██╔══██╗██╔══██║██║░░╚██╗██╔══╝░░██║░░░░░░╚═══██╗
██████╦╝██║░░██║╚██████╔╝███████╗███████╗██████╔╝
╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝╚══════╝╚═════╝░
""".strip()

you_win_text = """

██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
""".strip()

def introduction():
    clear_screen()
    print(colored(title, "blue"))
    print(colored(f"""\nBagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    (extended by me :3)(shio)

    I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
        Pico One digit is correct but in the wrong position.
        Fermi One digit is correct and in the right position.
        Bagels No digit is correct.

    For example, it the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.""", "blue"))

    print("\nI have thought up a number.")
    print(f"You have {MAX_GUESSES} guesses to get it.")

def main():
    introduction()
    while True:
        secret_num = get_secret_num()
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{num_guesses}")
                guess = input("> ")

            introduction()
            get_clues(num_guesses, guess, secret_num)

            if guess == secret_num:
                clear_screen()
                print(colored(you_win_text, "yellow"))
                print(f"Num of guesses taken: {num_guesses}")
                print(f"The secret number was: {secret_num}")
                break


            num_guesses += 1
            if num_guesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secret_num}")

        # Ask the player if the want to play again.
        print("Do you want to play again? (yes or no)")
        if input("> ").lower().startswith("y"):
            table.clear()
            main()
            
        else:
            break

    print("Thanks for playing!")

def get_secret_num():
    numbers = list("0123456789")
    random.shuffle(numbers)
    secret_num = ""

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])

    return "123"


def get_clues(num_guesses, guess, secret_num):
    if guess == secret_num:
        return

    clues = []


    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place
            clues.append("Pico")

    if len(clues) == 0:
        clues.append("Bagels") # There are no correct digits at all.

    clues.sort()
    table.append([f"GUESS: #{num_guesses}", guess, " ".join(clues)])
    print(tabulate(table, headers, tablefmt="rounded_grid"))
def clear_screen():
    os.system("cls") if platform == "win32" else os.system("clear") 


if __name__ == "__main__":
    main()
