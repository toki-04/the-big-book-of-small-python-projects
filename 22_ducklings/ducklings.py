import random
import shutil
import sys
import time

# CONSTANTS
PAUSE = 0.2
DENSITY = 0.10

DUCKLING_WIDTH = 5
LEFT = "left"
RIGHT = "right"
BEADY = "beady"
WIDE = "wide"
HAPPY = "happy"
ALOOF = "aloof"
CHUBBY = "chubby"
VERY_CHUBBY = "very chubby"
OPEN = "open"
CLOSED = "closed"
OUT = "out"
DOWN = "down"
UP = "up"
HEAD = "head"
BODY = "body"
FEET = "feet"

# Get terminal size
WIDTH = shutil.get_terminal_size()[0] - 1


def main():
    print("Duckling Screensaver, by Al Sweigart")
    print("Press Ctrl-C to quit...")
    time.sleep(2)

    duckling_lanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:
        for lane_num, duckling_obj in enumerate(duckling_lanes):
            # See if we should create a duckling in this lane:
            if (duckling_obj == None and random.random() <= DENSITY):
                # Place a duckling in this lane:
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj

            if duckling_obj != None:
                print(duckling_obj.get_next_body_part(), end="")
                if duckling_obj.part_to_display_next == None:
                    duckling_lanes[lane_num] = None

            else:
                print(' ' * DUCKLING_WIDTH, end="")

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


class Duckling:
    def __init__(self):
        """ Create a new duckling with random body features."""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            # Chubby ducklings can only have beady eyes
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        self.part_to_display_next = HEAD

    def get_head_str(self):
        """Returns the string of the duckling's head."""
        head_str = ''
        if self.direction == LEFT:
            # Get the mouth:
            if self.mouth == OPEN:
                head_str += '>'
            elif self.mouth == CLOSED:
                head_str += '='

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += '" '
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += '^^'
            elif self.eyes == ALOOF:
                head_str += '``'

            head_str += ') '  # Get the back of the head.

        if self.direction == RIGHT:
            head_str += ' ('  # Get the back of the head.

            # Get the eyes:
            if self.eyes == BEADY and self.body == CHUBBY:
                head_str += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                head_str += ' "'
            elif self.eyes == WIDE:
                head_str += "''"
            elif self.eyes == HAPPY:
                head_str += '^^'
            elif self.eyes == ALOOF:
                head_str += '``'

            # Get the mouth:
            if self.mouth == OPEN:
                head_str += '<'
            elif self.mouth == CLOSED:
                head_str += '='

        if self.body == CHUBBY:
            # Get an extra space so chubby ducklings are the same
            # width as very chubby ducklings.
            head_str += ' '

        return head_str

    def get_body_str(self):
        "Returns the string of the duckling's body"

        body_str = "("  # left side of the body

        if self.direction == LEFT:
            # Interior body space
            body_str += " "
            if self.body == CHUBBY:
                body_str += " "
            elif self.body == VERY_CHUBBY:
                body_str += "  "

            # Get the wings
            if self.wing == OUT:
                body_str += ">"
            elif self.wing == UP:
                body_str += "^"
            elif self.wing == DOWN:
                body_str += "v"

        if self.direction == RIGHT:
            if self.body == CHUBBY:
                body_str += " "
            elif self.body == VERY_CHUBBY:
                body_str += "  "

            # Get the wings
            if self.wing == OUT:
                body_str += "<"
            elif self.wing == UP:
                body_str += "^"
            elif self.wing == DOWN:
                body_str += "v"

        body_str += ")"  # right side of the body
        if self.body == CHUBBY:
            body_str += " "

        return body_str

    def get_feet_str(self):
        """Returns the string of the duckling's feet."""
        if self.body == CHUBBY:
            return " ^^  "
        elif self.body == VERY_CHUBBY:
            return " ^ ^ "

    def get_next_body_part(self):
        """Calls the appropriate display method for the next body
        part that needs to be displayed. Sets partToDisplayNext to
        None when finished."""

        if self.part_to_display_next == HEAD:
            self.part_to_display_next = BODY
            return self.get_head_str()
        elif self.part_to_display_next == BODY:
            self.part_to_display_next = FEET
            return self.get_body_str()
        elif self.part_to_display_next == FEET:
            self.part_to_display_next = None
            return self.get_feet_str()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
