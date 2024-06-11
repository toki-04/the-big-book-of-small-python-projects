import random
import sys
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module, which you")
    print("can install by following the instructions at")
    print("https://pypi.org/project/Bext/")
    sys.exit()

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUM_KELP = 30
NUM_FISH = 50
NUM_BUBBLERS = 20
FRAME_PER_SECOND = 4

FISH_TYPES = [
    {'right': ['><>'], 'left': ['<><']},
    {'right': ['>||>'], 'left': ['<||<']},
    {'right': ['>))>'], 'left': ['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'], 'left': ['<==-<']},
    {'right': [r'>\\>'], 'left': ['<//<']},
    {'right': ['><)))*>'], 'left': ['<*(((><']},
    {'right': ['}-[[[*>'], 'left': ['<*]]]-{']},
    {'right': [']-<)))b>'], 'left': ['<d(((>-[']},
    {'right': ['><XXX*>'], 'left': ['<*XXX><']},
    {
        'right': ['_.-._.-^=>', '.-._.-.^=>', '-._.-._^=>', '._.-._.^=>'],
        'left': ['<=^-._.-._', '<=^.-._.-.', '<=^_.-._.-', '<=^._.-._.']
    },
]

LONGEST_FISH_LENGTH = 10

LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg("black")
    bext.clear()

    # Generate the global variables
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generate_fish())

    # NOTE: Bubbles are drawn, but not the bubblers themselves.
    BUBBLERS = []
    for i in range(NUM_BUBBLERS):
        # Each bubbler starts at a random position
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))
    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelp_x = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {"x": kelp_x, "segments": []}

        # Generate each segment of the kelp:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp["segments"].append(random.choice(['(', ')']))
        KELPS.append(kelp)

    # Run the simulation:
    STEP = 1
    while True:
        simulate_aquarium()
        draw_aquarium()
        time.sleep(1 / FRAME_PER_SECOND)
        clear_aquarium()
        STEP += 1


def get_random_color():
    """Return a string of a random color."""
    return random.choice(('black', 'red', 'green', 'yellow', 'blue',
                          'purple', 'cyan', 'white'))


def generate_fish():
    """Returns a dictionary that represents a fish."""
    fish_type = random.choice(FISH_TYPES)

    # Set up colors for each character in the fish text:
    color_pattern = random.choice(("random", "head-tail", "single"))
    fish_length = len(fish_type["right"][0])
    if color_pattern == "random":
        colors = []
        for i in range(fish_length):
            colors.append(get_random_color())
    if color_pattern == "single" or color_pattern == "head-tail":
        colors = [get_random_color()] * fish_length  # All the same color.
    if color_pattern == "head-tail":  # Head/tail different from body.
        head_tail_color = get_random_color()
        colors[0] = head_tail_color
        colors[-1] = head_tail_color

    # Set up the rest of fish data structure:
    fish = {
        'right': fish_type['right'],
        'left': fish_type['left'],
        'colors': colors,
        'h_speed': random.randint(1, 6),
        'v_speed': random.randint(5, 15),
        'time_to_hdir_change': random.randint(10, 60),
        'time_to_vdir_change': random.randint(2, 20),
        'going_right': random.choice([True, False]),
        'going_down': random.choice([True, False])
    }

    # "x" is always the leftmost side of the fish body:
    fish["x"] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
    fish["y"] = random.randint(0, HEIGHT - 2)
    return fish


def simulate_aquarium():
    """Simulate the movements in the aquarium for one step."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Simulate the fish for one step:
    for fish in FISHES:
        if STEP % fish["h_speed"] == 0:
            if fish["going_right"]:
                if fish["x"] != RIGHT_EDGE:
                    fish["x"] += 1  # Move the fish right.
                else:
                    fish["going_right"] = False  # Turn the fish around.
                    fish["colors"].reverse()  # Turn the colors around.
            else:
                if fish["x"] != LEFT_EDGE:
                    fish["x"] -= 1  # Move the fish left.
                else:
                    fish["going_right"] = True  # Turn the fish .
                    fish["colors"].reverse()  # Turn the colors around.

        # Fish can randomly change their horizontal direction:
        fish["time_to_hdir_change"] -= 1
        if fish["time_to_hdir_change"] == 0:
            fish["time_to_hdir_change"] = random.randint(10, 60)
            fish["going_right"] = not fish["going_right"]

        # Move the fish vertically:
        if STEP % fish["v_speed"] == 0:
            if fish["going_down"]:
                if fish["y"] != BOTTOM_EDGE:
                    fish["y"] += 1  # Move the fish down.
                else:
                    fish["going_down"] = False  # Turn the fish around.

            else:
                if fish["y"] != TOP_EDGE:
                    fish["y"] -= 1  # Move the fish up.
                else:
                    fish["going_down"] = True  # Trun the fish around.

        # Fish can randomly change their vertical direction:
        fish["time_to_vdir_change"] -= 1
        if fish["time_to_vdir_change"] == 0:
            fish["time_to_vdir_change"] = random.randint(2, 20)
            fish["going_down"] = not fish["going_down"]

    # Generate bubbles from bubblers:
    for bubbler in BUBBLERS:
        if random.randint(1, 5) == 1:
            BUBBLES.append({"x": bubbler, "y": HEIGHT - 2})

    # Move the bubbles:
    for bubble in BUBBLES:
        dice_roll = random.randint(1, 6)
        if (dice_roll == 1) and (bubble["x"] != LEFT_EDGE):
            bubble["x"] -= 1  # bubble goes left.
        elif (dice_roll == 2) and (bubble["x"] != RIGHT_EDGE):
            bubble["x"] += 1  # bubble goes right.

        bubble["y"] -= 1  # The bubble always goes up.

    # Iterate over BUBBLES in reverse because I'm deleting from BUBBLES
    # while iterating over it

    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]["y"] == TOP_EDGE:  # Delete bubbles that reach the top.
            del BUBBLES[i]

    # Simulate the kelp waving for one step:
    for kelp in KELPS:
        for i, kelp_segment in enumerate(kelp["segments"]):
            # 1 in 20 change to change waving:
            if random.randint(1, 20) == 1:
                if kelp_segment == "(":
                    kelp["segments"][i] = ")"
                elif kelp_segment == ")":
                    kelp["segments"][i] = "("


def draw_aquarium():
    """Draw the aquarium on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Draw quit message.
    bext.fg("white")
    bext.goto(0, 0)
    print("Fish Tank, by Al Sweigart    CTRL-C to quit.", end="")

    # Draw the bubbles:
    bext.fg("white")
    for bubble in BUBBLES:
        bext.goto(bubble["x"], bubble["y"])
        print(random.choice(('o', 'O')), end='')

    # Draw the fish:
    for fish in FISHES:
        bext.goto(fish["x"], fish["y"])

        # Get the correct right or left-facing fish text.
        if fish["going_right"]:
            fish_text = fish["right"][STEP % len(fish["right"])]
        else:
            fish_text = fish["left"][STEP % len(fish["left"])]

        # Draw each character of the fish text in the right color.
        for i, fish_part in enumerate(fish_text):
            bext.fg(fish["colors"][i])
            print(fish_part, end="")

    # Draw the kelp:
    bext.fg("green")
    for kelp in KELPS:
        for i, kelp_segment in enumerate(kelp["segments"]):
            if kelp_segment == "(":
                bext.goto(kelp["x"], BOTTOM_EDGE - i)
            elif kelp_segment == ")":
                bext.goto(kelp["x"] + 1, BOTTOM_EDGE - i)
            print(kelp_segment, end="")

    # Draw the sand on the bottom:
    bext.fg("yellow")
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end="")  # Draws sand.

    sys.stdout.flush()  # (Required for bext-using programs.)


def clear_aquarium():
    """Draw empty spaces over everything on the screen."""
    global FISHES, BUBBLERS, BUBBLES, KELP

    # Draw the bubbles:
    for bubble in BUBBLES:
        bext.goto(bubble["x"], bubble["y"])
        print(" ", end="")

    # Draw the fish:
    for fish in FISHES:
        bext.goto(fish["x"], fish["y"])

        # Draw each character of the fish text in the right color.
        print(" " * len(fish["left"][0]), end="")

    # Draw the kelp:
    for kelp in KELPS:
        for i, kelp_segment in enumerate(kelp["segments"]):
            bext.goto(kelp["x"], HEIGHT - 2 - i)
            print("  ", end="")

    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
