import sys
import random

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6

WHITE = "white"
BLACK = "black"
RED = "red"
YELLOW = "yellow"
BLUE = "blue"

width, height = bext.size()
width -= 1
height -= 3

while True:
    canvas = {}

    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE

    number_of_segments_to_delete = 0

    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < width - MIN_X_INCREASE:
        number_of_segments_to_delete += 1

        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < height - MIN_Y_INCREASE:
        number_of_segments_to_delete += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    number_of_rectangles_to_paint = number_of_segments_to_delete - 3
    number_of_segments_to_delete = int(number_of_segments_to_delete * 1.5)

    for i in range(number_of_segments_to_delete):
        while True:
            start_x = random.randint(1, width - 2)
            start_y = random.randint(1, height - 2)

            if canvas[(start_x, start_y)] == WHITE:
                continue

            if (canvas[(start_x - 1, start_y)] == WHITE and
                    canvas[(start_x + 1, start_y)] == WHITE):
                orientation = "vertical"
            elif (canvas[(start_x, start_y - 1)] == WHITE and
                    canvas[(start_x, start_y + 1)] == WHITE):
                orientation = "horizontal"
            else:
                continue

            points_to_delete = [(start_x, start_y)]

            can_delete_segment = True

            if orientation == "vertical":
                for change_y in (-1, 1):
                    y = start_y

                    while 0 < y < height - 1:
                        y += change_y

                        if (canvas[(start_x - 1, y)] == BLACK and
                                canvas[(start_x + 1), y] == BLACK):
                            break
                        elif ((canvas[(start_x - 1, y)] == WHITE and
                                canvas[(start_x + 1, y)] == BLACK) or
                                (canvas[(start_x - 1, y)] == BLACK and
                                 canvas[(start_x + 1, y)] == WHITE)):

                            can_delete_segment = False
                            break
                        else:
                            points_to_delete.append((start_x, y))

            elif orientation == "horizontal":
                for change_x in (-1, 1):
                    x = start_x

                    if (canvas[(x, start_y - 1)] == BLACK and
                            canvas[(x, start_y + 1) == BLACK]):
                        break

                    elif ((canvas[(x, start_y - 1)] == WHITE and
                            canvas[(x, start_y + 1)] == BLACK) or
                            (canvas[(x, start_y - 1)] == BLACK and
                             canvas[(x, start_y + 1)] == WHITE)):

                        can_delete_segment = False
                        break

                    else:
                        points_to_delete.append((x, start_y))

            if not can_delete_segment:
                continue

            break

        for x, y in points_to_delete:
            canvas[(x, y)] = WHITE

    for x in range(width):
        canvas[(x, 0)] = BLACK
        canvas[(x, height - 1)] = BLACK

    for y in range(height):
        canvas[(0, y)] = BLACK
        canvas[(width - 1, y)] = BLACK

    for i in range(number_of_rectangles_to_paint):
        while True:
            start_x = random.randint(1, width - 2)
            start_y = random.randint(1, height - 2)

            if canvas[(start_x, start_y)] != WHITE:
                continue
            else:
                break

        color_to_paint = random.choice([RED, YELLOW, BLUE, BLACK])
        points_to_paint = set([(start_x, start_y)])

        while len(points_to_paint) > 0:
            x, y = points_to_paint.pop()
            canvas[(x, y)] = color_to_paint
            if canvas[(x - 1, y)] == WHITE:
                points_to_paint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                points_to_paint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                points_to_paint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                points_to_paint.add((x, y + 1))

    for y in range(height):
        for x in range(width):
            bext.bg(canvas[(x, y)])
            print(" ", end="")

        print()

    try:
        input("Press Enter for another work of art, or Ctrl-C to quit.")
    except KeyboardInterrupt:
        sys.exit()
