"""Bitmap Message, by Al Sweigart al@inventwithpython.com
Displays a text message according to the provided bitmap image.
View this code at https://nostarch.com/big-book-small-python-projects
Bitmap Message 13
Tags: tiny, beginner, artistic"""

import sys

# (!)
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Bitmap Message, by AI Sweigart al@inventwithpython.com")
print("Enter the message to display with the bitmap.")

message: str = input('> ')
if message == "":
    sys.exit("")

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line: 
    for i, bit in enumerate(line):
        if bit == " ":
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end="")
    print()



