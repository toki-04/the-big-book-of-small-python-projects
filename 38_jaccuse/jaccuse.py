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
# import pprint
# pprint.pprint(clues)
# pprint.pprint(zophie_clues)
# print("culprit = ", culprit)

# START OF THE GAME
print("""J'ACCUSE! (a mystery game)")
By Al Sweigart al@inventwithpython.com
Inspired by Homestar Runner\'s "Where\'s an Egg?" game
You are the world-famous detective Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. Then you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")

input("Press Enter to begin...")

start_time = time.time()
end_time = start_time + TIME_TO_SOLVE

while True:
    if time.time() > end_time or accusation_left == 0:
        if time.time() > end_time:
            print("You have run out of time!")
        elif accusation_left == 0:
            print("You have accused to many innocent people!")

        culprit_index = SUSPECTS.index(culprit)
        print("It was {} at the {} with the {} who catnapped her!".format(culprit,
                                                                          PLACES[culprit_index], ITEMS[culprit_index]))

    print()
    minutes_left = int(end_time - time.time()) // 60
    seconds_left = int(end_time - time.time()) % 60
    print("Time Left: {} min, {} sec".format(minutes_left, seconds_left))

    if current_location == "TAXI":
        print("  You are in your TAXI, Where do you want to go?")
        for place in sorted(PLACES):
            place_info = ""
            if place in visited_places:
                place_info = visited_places[place]
            name_label = "(" + place[0] + ")" + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print("{} {}{}".format(name_label, spacing, place_info))
        print("(Q)UIT GAME")

        while True:
            response = input("> ").upper()
            if response == "":
                continue
            if response == "Q":
                print("Thanks for playing!")
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break

        current_location = PLACE_FIRST_LETTERS[response]
        continue

    print("  You are at the {}.".format(current_location))
    current_location_index = PLACES.index(current_location)
    the_person_here = SUSPECTS[current_location_index]
    the_item_here = ITEMS[current_location_index]

    print("  {} with the {} is here.".format(the_person_here, the_item_here))

    if the_person_here not in known_suspects_and_items:
        known_suspects_and_items.append(the_person_here)
    if ITEMS[current_location_index] not in known_suspects_and_items:
        known_suspects_and_items.append(ITEMS[current_location_index])
    if current_location not in visited_places.keys():
        visited_places[current_location] = "({}, {})".format(
            the_person_here.lower(), the_item_here.lower())

    if the_person_here in accused_suspects:
        print('They are offended that you accused them,')
        print('and will not help with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        current_location = "TAXI"
        continue

    # Display menu of known suspects & items to ask about:
    print()
    print('(J) "J\'ACCUSE!" ({} accusations left)'.format(accusation_left))
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')

    for i, suspect_or_item in enumerate(known_suspects_and_items):
        print('({}) Ask about {}'.format(i + 1, suspect_or_item))

    while True:
        response = input("> ").upper()
        if response in 'JZT' or (response.isdecimal() and 0 < int(response) <=
                                 len(known_suspects_and_items)):
            break

    if response == "J":
        accusation_left -= 1
        if the_person_here == culprit:
            print('You\'ve cracked the case, Detective!')
            print('It was {} who had catnapped ZOPHIE THE CAT.'.format(culprit))
            minutes_taken = int(time.time() - start_time) // 60
            seconds_taken = int(time.time() - start_time) % 60
            print('Good job! You solved it in {} min, {} sec.'.format(
                minutes_taken, seconds_taken))
            sys.exit()
        else:
            accused_suspects.append(the_person_here)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            current_location = 'TAXI'

    elif response == "Z":
        if the_person_here not in zophie_clues:
            print('"I don\'t know anything about ZOPHIE THE CAT."')
        elif the_person_here in zophie_clues:
            print('  They give you this clue: "{}"'.format(
                zophie_clues[the_person_here]))
            if zophie_clues[the_person_here] not in known_suspects_and_items and zophie_clues[the_person_here] not in PLACES:
                known_suspects_and_items.append(zophie_clues[the_person_here])

    elif response == "T":
        current_location = "TAXI"
        continue

    else:
        things_being_asked_about = known_suspects_and_items[int(response) - 1]
        if things_being_asked_about in (the_person_here, the_item_here):
            print('  They give you this clue: "No Comment."')
        else:
            print(' They give you this clue: "{}"'.format(
                clues[the_person_here][things_being_asked_about]))

            if clues[the_person_here][things_being_asked_about] not in known_suspects_and_items and clues[the_person_here][things_being_asked_about] not in PLACES:
                known_suspects_and_items.append(
                    clues[the_person_here][things_being_asked_about])

    input("Press Enter to continue...")
