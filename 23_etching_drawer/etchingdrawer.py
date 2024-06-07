import shutil
import sys

# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR = chr(9532)  # Character 9532 is '┼'
# A list of chr() codes is at https://inventwithpython.com/chr

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x, y) integer tuples for the coordinate,
and the value is a set of letters W, A, S, D that tell what kind of line
should be drawn."""
canvas = {}
cursor_x = 0
cursor_y = 0


def get_canvas_string(canvas_data, cx, cy):
    """Returns a multiline string of the line drawn in canvasData."""
    canvas_str = ""

    """canvasData is a dictionary with (x, y) tuple keys and values that
    are sets of 'W', 'A', 'S', and/or 'D' strings to show which
    directions the lines are drawn at each xy point."""

    for row_num in range(CANVAS_HEIGHT):
        for column_num in range(CANVAS_WIDTH):
            if column_num == cx and row_num == cy:
                canvas_str += "#"
                continue

            # Add the line character for tis point to canvas_str
            cell = canvas_data.get((column_num, row_num))
            if cell in (set(["W", "S"]), set(["W"]), set(["S"])):
                canvas_str += UP_DOWN_CHAR
            elif cell in (set(["A", "D"]), set(["A"]), set(["D"])):
                canvas_str += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvas_str += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvas_str += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvas_str += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvas_str += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvas_str += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvas_str += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvas_str += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvas_str += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvas_str += CROSS_CHAR
            elif cell == None:
                canvas_str += " "

        canvas_str += "\n"
    return canvas_str


moves = []
while True:
    # Draw the lines based on the data in canvas:
    print(get_canvas_string(canvas, cursor_x, cursor_y))

    print("WASD kes to move, H for help, C to clear, " +
          "F to save, or QUIT.")
    response = input("> ").upper()

    if response == "QUIT":
        print("Thanks for playing!")
        sys.exit()

    elif response == "H":
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == "C":
        canvas = {}  # Erase the canvas data.
        moves.append("C")  # Record this move.
    elif response == "F":
        # Save the canvas string to a text file:
        try:
            print("Enter filename to save to:")
            filename = input("> ")

            # Make sure the filename ends with .txt
            if not filename.endswith(".txt"):
                filename += ".txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write("".join(moves) + "\n")
                file.write(get_canvas_string(canvas, None, None))
        except:
            print("ERROR: Could not save file.")

    for command in response:
        if command not in ("W", "A", "S", "D"):
            continue

        moves.append(command)

        # The first line we add needs to form a full line:
        if canvas == {}:
            if command in ("W", "S"):
                canvas[(cursor_x, cursor_y)] = set(["W", "S"])
            elif command in ("A", "D"):
                canvas[(cursor_x, cursor_y)] = set(["A", "D"])

        # Update x and y:
        if command == "W" and cursor_y > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y - 1
        elif command == "S" and cursor_y < CANVAS_HEIGHT - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y = cursor_y + 1
        elif command == "A" and cursor_x > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x - 1
        elif command == "D" and cursor_x < CANVAS_WIDTH - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x = cursor_x + 1
        else:
            # If the cursor doesn't move because it would have moved off
            # the edge of the canvas, then don't change the set at
            # canvas[(cursorX, cursorY)].
            continue

        # If there's no set for (cursor_x, cursor_y), add an empty set:
        if (cursor_x, cursor_y) not in canvas:
            canvas[(cursor_x, cursor_y)] = set()

        # Add the direction string to this xy point's set:
        if command == "W":
            canvas[(cursor_x, cursor_y)].add("S")
        elif command == "S":
            canvas[(cursor_x, cursor_y)].add('W')
        elif command == "A":
            canvas[(cursor_x, cursor_y)].add("D")
        elif command == "D":
            canvas[(cursor_x, cursor_y)].add("A")
