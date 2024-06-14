import sys

EMPTY_SPACE = "."
PLAYER_X = "X"
PLAYER_O = "O"

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH


def main():
    print("""Four in a Row, by Al Sweigart al@inventwithpython.com

Two players take turns dropping tiles into one of seven columns, trying
to make four in a row horizontally, vertically, or diagonally.
""")

    # Set up a new game
    game_board = get_new_board()
    player_turn = PLAYER_X

    while True:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        game_board[player_move] = player_turn

        # Check for a win or tie:
        if is_winner(player_turn, game_board):
            display_board(game_board)
            print("Player "+player_turn+" has won!")
            sys.exit()
        elif is_full(game_board):
            display_board(game_board)
            print("There is a tie!")
            sys.exit()

        # Switch turns to other player:
        if player_turn == PLAYER_X:
            player_turn = PLAYER_O
        elif player_turn == PLAYER_O:
            player_turn = PLAYER_X


def get_new_board():
    """Returns a dictionary that represents a Four in a Row board."""

    board = {}
    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT):
            board[(column_index, row_index)] = EMPTY_SPACE
    return board


def display_board(board):
    """Display the board and its tiles on the screen."""

    tile_chars = []
    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            tile_chars.append(board[(column_index, row_index)])

    # Display hte board:
    print("""
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+""".format(*tile_chars))


def ask_for_player_move(player_tile, board):
    """Let a player select a column on the board to drop a tile into.

    Returns a tuple of the (column, row) that the tile falls into."""

    while True:
        print("Player {}, endter a column or QUIT:".format(player_tile))
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()

        if response not in COLUMN_LABELS:
            print("Enter a number from 1 to {}.").format(BOARD_WIDTH)
            continue

        column_index = int(response) - 1

        # if the column is full, ask for a move again
        if board[(column_index, 0)] != EMPTY_SPACE:
            print("That column is full, select another one.")
            continue

        # Starting from the bottom, find the first empty space.
        for row_index in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return (column_index, row_index)


def is_full(board):
    """Returns True if the board has no empty spaces, otherwise return False"""

    for row_index in range(BOARD_HEIGHT):
        for column_index in range(BOARD_WIDTH):
            if board[(column_index, row_index)] == EMPTY_SPACE:
                return False
    return True


def is_winner(player_tile, board):
    """Returns True if player_tile has four tiles in a row on board
    otherwise returns False."""

    # Go through the entire board, checking for four-in-a-row:
    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT):
            # Check for horizontal four-in-a-row going right:
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index)]
            tile_3 = board[(column_index + 2, row_index)]
            tile_4 = board[(column_index + 3, row_index)]

            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH):
        for row_index in range(BOARD_HEIGHT - 3):
            # Check for vertical four-in-a-row going down:
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index, row_index + 1)]
            tile_3 = board[(column_index, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]

            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    for column_index in range(BOARD_WIDTH - 3):
        for row_index in range(BOARD_HEIGHT - 3):
            # Check for four-in-a-row going right-down diagonal:
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index + 1)]
            tile_3 = board[(column_index + 2, row_index + 2)]
            tile_4 = board[(column_index + 3, row_index + 3)]

            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

            # Check for four-in-a-row going left-down-diagonal:
            tile_1 = board[(column_index + 3, row_index)]
            tile_2 = board[(column_index + 2, row_index + 1)]
            tile_3 = board[(column_index + 1, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]

            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True

    return False


if __name__ == "__main__":
    main()
