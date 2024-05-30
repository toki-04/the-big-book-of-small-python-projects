def main() -> None:
    print("Diamonds, by Al Sweigart al@inventwithpython.com")

    # Display diamonds of sizes 0 through 6:
    for diamond_size in range(0, 6):
        display_outline_diamond(diamond_size)
        print()
        display_filled_diamond(diamond_size)
        print()


def display_outline_diamond(size: int) -> None:
    # Display the top half of the diamond:
    for i in range(size):
        print(" " * (size - i - 1), end='')  # Left side space.
        print("/", end="")  # Left side of diamond.
        print(" " * (i * 2), end="")  # Interior of diamond
        print("\\")  # Right side of diamond.

    for i in range(size):
        print(" " * i, end="")  # Left side space.
        print("\\", end="")  # Left side of diamond.
        print(" " * ((size - i - 1) * 2), end="")  # Interior of diamond.
        print("/")  # Right side of diamond


def display_filled_diamond(size: int) -> None:
    # Display the top half of the diamond
    for i in range(size):
        print(" " * (size - i - 1), end="")  # Left side space.
        print("/" * (i + 1), end="")  # Left half of diamond.
        print("\\" * (i+1))  # Right half of diamond

    # Display the bottom half of the diamond:
    for i in range(size):
        print(" " * i, end="")  # Left side space.
        print("\\" * (size - i), end="")  # Left side of diamond
        print("/" * (size - i))  # Right side of diamond.


if __name__ == "__main__":
    main()
