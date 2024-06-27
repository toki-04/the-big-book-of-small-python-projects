import random

GOLD = "GOLD"
SILVER = "SILVER"
BRONZE = "BRONZE"

STAR_FACE = ["+-----------+",
             "|     .     |",
             "|    ,O,    |",
             "| 'ooOOOoo' |",
             "|   `OOO`   |",
             "|   O' 'O   |",
             "+-----------+"]


SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \\   |',
              '|  |() ()|  |',
              '|   \\ ^ /   |',
              '|    VVV    |',
              '+-----------+']

QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']

FACE_WIDTH = 13
FACE_HEIGHT = 7

print("""Lucky Stars, by Al Sweigart al@inventwithpython.com

A "press your luck" game where you roll dice with Stars, Skulls, and
Question Marks.

On your turn, you pull three random dice from the dice cup and roll
them. You can roll Stars, Skulls, and Question Marks. You can end your
turn and get one point per Star. If you choose to roll again, you keep
the Question Marks and pull new dice to replace the Stars and Skulls.
If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before
the game ends. Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is
even.
""")

print("How many players are there?")
while True:
    response = input("> ")
    if response.isdecimal() and int(response) > 1:
        num_players = int(response)
        break

    print("Please enter a number larger than 1.")

player_names = []
player_scores = {}

for i in range(num_players):
    while True:
        print('What is player #' + str(i + 1) + '\'s name?')
        response = input("> ")
        if response != "" and response not in player_names:
            player_names.append(response)
            player_scores[response] = 0
            break
        print("Please enter a name.")
print()

turn = 0
end_game_with = None

while True:
    print()
    print("SCORES: ", end="")
    for i, name in enumerate(player_names):
        print(name + ' = ' + str(player_scores[name]), end='')
        if i != len(player_names) - 1:
            print(", ", end="")
    print("\n")

    stars = 0
    skulls = 0

    cup = ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)
    hand = []
    print("It is " + player_names[turn] + "\'s turn.")

    while True:
        print()

        if (3 - len(hand)) > len(cup):
            print('There aren\'t enough dice left in the cup to ' +
                  'continue ' + player_names[turn] + '\'s turn.')
            break

        random.shuffle(cup)
        while len(hand) < 3:
            hand.append(cup.pop())

        roll_results = []
        for dice in hand:
            roll = random.randint(1, 6)
            if dice == GOLD:
                if 1 <= roll <= 3:
                    roll_results.append(STAR_FACE)
                    stars += 1
                elif 4 <= roll <= 5:
                    roll_results.append(QUESTION_FACE)
                else:
                    roll_results.append(SKULL_FACE)
                    skulls += 1

            if dice == SILVER:
                if 1 <= roll <= 2:
                    roll_results.append(STAR_FACE)
                    stars += 1
                elif 3 <= roll <= 4:
                    roll_results.append(QUESTION_FACE)
                else:
                    roll_results.append(SKULL_FACE)
                    skulls += 1

            if dice == BRONZE:
                if roll == 1:
                    roll_results.append(STAR_FACE)
                    stars += 1
                elif 2 <= roll <= 4:
                    roll_results.append(QUESTION_FACE)
                else:
                    roll_results.append(SKULL_FACE)
                    skulls += 1

        for line_num in range(FACE_HEIGHT):
            for dice_num in range(3):
                print(roll_results[dice_num][line_num] + " ", end="")
            print()

        for dice_type in hand:
            print(dice_type.center(FACE_WIDTH) + " ", end="")
        print()

        print("Stars collected:", stars, " Skulls collected:", skulls)

        if skulls >= 3:
            print('3 or more skulls means you\'ve lost your stars!')
            input('Press Enter to continue...')
            break

        print(player_names[turn] + ", do you want to roll again? Y/N")
        while True:
            response = input("> ").upper()
            if response != "" and response[0] in ("Y", "N"):
                break
            print("Please enter Yes or No.")

        if response.startswith("N"):
            print(player_names[turn], "got", stars, "stars!")
            player_scores[player_names[turn]] += stars

            if (end_game_with == None and player_scores[player_names[turn]] >= 13):
                print('\n\n' + ('!' * 60))
                print(player_names[turn] + ' has reached 13 points!!!')
                print('Everyone else will get one more turn!')
                print(('!' * 60) + '\n\n')
                end_game_with = player_names[turn]
            input("Press Enter to continue...")
            break

        next_hand = []
        for i in range(3):
            if roll_results[i] == QUESTION_FACE:
                next_hand.append(hand[i])
        hand = next_hand

    turn = (turn + 1) % num_players

    if end_game_with == player_names[turn]:
        break

print("The game has ended...")

print()
print("SCORES: ", end="")
for i, name in enumerate(player_names):
    print(name + " = " + str(player_scores[name]), end="")
    if i != len(player_names) - 1:
        print(", ", end="")
print("\n")

highest_score = 0
winners = []

for name, score in player_scores.items():
    if score > highest_score:
        highest_score = score
        winners.append(name)
    elif score == highest_score:
        winners.append(name)

if len(winners) == 1:
    print("The winner is " + winners[0] + "!!!")
else:
    print("The winners are: " + ", ".join(winners))

print("Thanks for playing")
