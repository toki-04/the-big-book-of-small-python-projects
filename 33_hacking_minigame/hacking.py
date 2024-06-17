import random
import sys

# The garbage filler characters for the "computer memory" display.
GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|;:,.<>?/'

with open("sevenletterwords.txt") as word_list_file:
    WORDS = word_list_file.readlines()

for i in range(len(WORDS)):
    WORDS[i] = WORDS[i].strip().upper()


def main():
    """Run a single game of Hacking."""
    print('''Hacking Minigame, by Al Sweigart al@inventwithpython.com
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n''')

    input("Press Enter to begin...")

    game_words = get_words()

    computer_memory = get_computed_memory_string(game_words)
    secret_password = random.choice(game_words)

    print(computer_memory)

    for tries_remaining in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, tries_remaining)
        if player_move == secret_password:
            print("A C C E S S  G R A N T E D")
            return
        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print('Access Denied ({}/7 correct)'.format(num_matches))

    print('Out of tries. Secret password was {}.'.format(secret_password))


def get_words():
    """Return a list of 12 words that could possibly be the password.

    The secret password will be the first word in the list.
    To make the game fair, we try to ensure that there are words with
    a range of matching numbers of letters as the secret word."""

    secret_password = random.choice(WORDS)
    words = [secret_password]

    while len(words) < 3:
        random_word = get_one_word_except(words)

        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)

    for i in range(500):
        if len(words) == 5:
            break

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 3:
            words.append(random_word)

    for i in range(500):
        if len(words) == 12:
            break

        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) != 0:
            words.append(random_word)

    while len(words) < 12:
        random_word = get_one_word_except(words)
        words.append(random_word)

    assert len(words) == 12
    return words


def get_one_word_except(blocklist=None):
    """Returns a random word from WORDS that isn't in blocklist."""
    if blocklist == None:
        blocklist = []

    while True:
        random_word = random.choice(WORDS)
        if random_word not in blocklist:
            return random_word


def num_matching_letters(word_1, word_2):
    """Returns the number of matching letters in these two words."""
    matches = 0
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            matches += 1
    return matches


def get_computed_memory_string(words):
    """Return a string representing the "computer memory"."""
    lines_with_words = random.sample(range(16*2), len(words))
    memory_address = 16 * random.randint(0, 4000)

    computer_memory = []
    next_word = 0
    for line_num in range(16):
        left_half = ""
        right_half = ""
        for j in range(16):
            left_half += random.choice(GARBAGE_CHARS)
            right_half += random.choice(GARBAGE_CHARS)

        if line_num in lines_with_words:
            insertion_index = random.randint(0, 9)
            left_half = (left_half[:insertion_index] + words[next_word]
                         + left_half[insertion_index + 7:])
            next_word += 1
        if line_num + 16 in lines_with_words:
            insertion_index = random.randint(0, 9)
            right_half = (right_half[:insertion_index] + words[next_word]
                          + right_half[insertion_index + 7:])
            next_word += 1

        computer_memory.append("0x" + hex(memory_address)[2:].zfill(4)
                               + "  " + left_half + "    "
                               + "0x" + hex(memory_address +
                                            (16*16))[2:].zfill(4)
                               + "  " + right_half)

        memory_address += 16

    return "\n".join(computer_memory)


def ask_for_player_guess(words, tries):
    while True:
        print("Enter password: ({} tries remaining)".format(tries))
        guess = input("> ").upper()
        if guess in words:
            return guess
        print('That is not one of the possible passwords listed above.')
        print('Try entering "{}" or "{}".'.format(words[0], words[1]))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
