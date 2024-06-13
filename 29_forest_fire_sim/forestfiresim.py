import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

WIDTH = 79
HEIGHT = 22

TREE = "A"
FIRE = "W"
EMPTY = " "

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = create_new_forest()
    bext.clear()

    while True:
        display_forest(forest)

        next_forest = {
            "width": forest["width"],
            "height": forest["height"]
        }

        for x in range(forest["width"]):
            for y in range(forest["height"]):
                if (x, y) in next_forest:
                    continue

                if ((forest[(x, y)] == EMPTY)
                        and (random.random() <= GROW_CHANCE)):
                    next_forest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                        and (random.random() <= FIRE_CHANCE)):
                    next_forest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x+ix, y+iy)) == TREE:
                                next_forest[(x+ix, y+iy)] = FIRE
                    next_forest[(x, y)] = forest[(x, y)]
                else:
                    next_forest[(x, y)] = forest[(x, y)]

        forest = next_forest

        time.sleep(PAUSE_LENGTH)


def create_new_forest():
    """Returns a dictionary for a new forest data structure."""
    forest = {"width": WIDTH, "height": HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    return forest


def display_forest(forest):
    """Display the forest data structure on the screen."""
    bext.goto(0, 0)
    for y in range(forest["height"]):
        for x in range(forest["width"]):
            if forest[(x, y)] == TREE:
                bext.fg("green")
                print(TREE, end="")
            elif forest[(x, y)] == FIRE:
                bext.fg("red")
                print(FIRE, end="")
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end="")
        print()
    bext.fg("reset")
    print("Grow chance: {}% ".format(GROW_CHANCE * 100), end='')
    print("Lightning chance: {}% ".format(FIRE_CHANCE * 100), end='')
    print("Press Ctrl-C to quit.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
