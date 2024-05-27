import copy
import random
import sys
import time

# Set up the constants:
WIDTH: int = 79
HEIGHT: int = 20

# (!) Try changing ALIVE to "#" or another character:
# (!) Try changing DEAD to "."" or another character:
ALIVE: str = "O"  # The chracter representing a living cell
DEAD: str = " "  # The character representing a dead cell

next_cells: dict = {}
# Put random deead and alive cell into next_cells:
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            # 50/50 chance for starting cells being alived or dead.
            next_cells[(x, y)] = ALIVE
        else:
            next_cells[(x, y)] = DEAD

while True:
    # Each iteration of this loop is a step of the simulation
    print("\n" * 50)
    cells = copy.deepcopy(next_cells)

    # Print  cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end="")
        print()
    print("Press Ctrl-C to quit.")

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they
            # wrap around the edge:
            left: int = (x - 1) % WIDTH
            right: int = (x + 1) % WIDTH
            above: int = (y - 1) % HEIGHT
            below: int = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            num_neighbors = 0
            if cells[(left, above)] == ALIVE:
                num_neighbors += 1  # Top-left neighbor is alive.
            if cells[(x, above)] == ALIVE:
                num_neighbors += 1  # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                num_neighbors += 1  # Top-right neighbor is alive.
            if cells[(left, y)] == ALIVE:
                num_neighbors += 1  # Left neighbor is alive.
            if cells[(right, y)] == ALIVE:
                num_neighbors += 1  # Right neighbor is alive.
            if cells[(left, below)] == ALIVE:
                num_neighbors += 1  # Bottom-left neighbor is alive.
            if cells[(x, below)] == ALIVE:
                num_neighbors += 1  # Bottom neighbor is alive.
            if cells[(right, below)] == ALIVE:
                num_neighbors += 1  # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (num_neighbors == 2
                                           or num_neighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and num_neighbors == 3:
                # Dead cells with 3 neighbors become alive:
                next_cells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                next_cells[(x, y)] = DEAD

            ############################################

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("Conway's Game of Live")
        print("By Al Sweigart al@inventwithpython.com")
        sys.exit()
