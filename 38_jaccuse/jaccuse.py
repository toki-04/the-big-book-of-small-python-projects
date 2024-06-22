import time
import random
import sys

SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR',
            'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT',
            'CECIL EDGAR VANDERTON']

ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE',
         'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']

PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY',
          'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']

TIME_TO_SOLVE = 300

PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0

for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Sanity Check
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9

assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

known_suspects_and_items = []
visited_places = {}
current_location = "TAXI"
accused_suspects = []
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusation_left = 3
culprit = random.choice(SUSPECTS)

random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

clues = {}

for i, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue

    clues[interviewee] = {}
    clues[interviewee]["debug_liar"] = False
    for item in ITEMS:
        if random.randint(0, 1) == 0:
            clues[interviewee][item] = PLACES[ITEMS.index(item)]
        else:
            clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]

    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
        else:
            clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]

for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue

    clues[interviewee] = {}
    clues[interviewee]["debug_liar"] = True

    for item in ITEMS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    break

        else:
            while True:
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    break

    for suspect in SUSPECTS:
        if random.randint(0, 1) == 0:
            while True:
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[ITEMS.index(item)]:
                    break

        else:
            while True:
                clues[interviewee][suspect] = random.choice(ITEMS)
                if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                    break


zophie_clues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kind_of_clue = random.randint(1, 3)
    if kind_of_clue == 1:
        if interviewee not in liars:
            zophie_clues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                if zophie_clues[interviewee] != culprit:
                    break

    elif kind_of_clue == 2:
        if interviewee not in liars:
            zophie_clues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = random.choice(PLACES)
                if zophie_clues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    break

    elif kind_of_clue == 3:
        if interviewee not in liars:
            zophie_clues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophie_clues[interviewee] = random.choice(ITEMS)
                if zophie_clues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    break

# EXPERIMENT: Uncomment this code to view the clue data structures:
