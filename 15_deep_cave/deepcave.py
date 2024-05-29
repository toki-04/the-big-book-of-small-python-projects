import random
import sys
import time


# Set up the constants:
WIDTH: int = 70          # (!) Try changing this to 10 or 30.
PAUSE_AMOUNT: int = 0.05  # (!) Try changin this to 0 or 1.0.

print("Deep Cave, by Al Sweigart al@inventwithpyhon.com")
print("Press Ctrl-C to stop.")
time.sleep(2)

left_width: int = 20
gap_width: int = 10

while True:
    # Display the tunnel segment:
    right_width: int = WIDTH - gap_width - left_width
    print(("#" * left_width) + (" " * gap_width) + ("#" * right_width))

    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    # Adjust the left side width:
    dice_roll: int = random.randint(1, 6)

    if dice_roll == 1 and left_width > 1:
        left_width = left_width - 1  # Decrease the left side width.
    elif dice_roll == 2 and left_width + gap_width < WIDTH - 1:
        gap_width = gap_width + 1
    else:
        pass
