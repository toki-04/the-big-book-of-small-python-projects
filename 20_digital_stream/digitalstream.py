import random
import shutil
import sys
import time

# Set up the constants
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14
PAUSE = 0.1
STREAM_CHARS = ["0", "1"]

# Density can range from 0.0 to 1.0:
DENSITY = 0.02

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

print("Digital Stream, by Al Sweigart al@inventwithpython.com")
print("Press Ctrl-C to quit.")
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # Restart a steam on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH,
                                                MAX_STREAM_LENGTH)

            # Display an empty space or a 1/0 character
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end="")
                columns[i] -= 1
            else:
                print(" ", end="")

        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
