import copy
import sys
import os

WALL = "#"
EMPTY = " "
START = "S"
EXIT = "E"
BLOCK = chr(9617)
NORTH = "NORTH"
SOUTH = "SOUTH"
EAST = "EAST"
WEST = "WEST"


def wall_str_to_wall_dict(wall_str):
    """Takes a string representation of a wall drawing (like those in
    ALL_OPEN or CLOSED) and returns a representation in a dictionary
    with (x, y) tuples as keys and single-character strings of the
    character to draw at that x, y location."""

    wall_dict = {}
    height = 0
    width = 0

    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y

        for x, character in enumerate(line):
            if x > width:
                width = x
            wall_dict[(x, y)] = character

    wall_dict["height"] = height + 1
    wall_dict["width"] = width + 1
    return wall_dict


EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

ALL_OPEN = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())

CLOSED = {}
CLOSED['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
_____'''.strip())

CLOSED['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.'''.strip())

CLOSED['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())

CLOSED['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
\..
.\.'''.strip())

CLOSED['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())

CLOSED['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())