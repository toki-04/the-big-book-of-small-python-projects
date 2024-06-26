import random

try:
    import pyperclip
except ImportError:
    pass


def main():
    print('''L3375P34]< (leetspeek)
    By Al Sweigart al@inventwithpython.com

    Enter your leet message:''')
    english = input('> ')
    print()
    leetspeak = english_to_leetspeak(english)
    print(leetspeak)

    try:
        pyperclip.copy(leetspeak)
        print('(Copied leetspeak to clipboard.)')
    except NameError:
        pass


def english_to_leetspeak(message):
    """Convert the English string in message and return leetspeak."""

    char_mapping = {
        'a': ['4', '@', '/-\\'], 'c': ['('], 'd': [' |)'], 'e': ['3'],
        'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],
        'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],
        'v': ['\\/']
    }

    leetspeak = ''

    for char in message:
        if char.lower() in char_mapping and random.random() <= 0.70:
            possible_leet_replacements = char_mapping[char.lower()]
            leet_replacements = random.choice(possible_leet_replacements)
            leetspeak = leetspeak + leet_replacements
    else:
        leetspeak = leetspeak + char

    return leetspeak


if __name__ == "__main__":
    main()
