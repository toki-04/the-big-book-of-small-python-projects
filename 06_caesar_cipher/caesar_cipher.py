import pyperclip

SYMBOLS: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Caesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The Caesar cipher encrypts letters by shifting them over by a')
print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True: # Keep asking until the user enters e or d.
    print("Do you want to (e)ncrypt or (d)ecrypt?")

    response: str = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d.")

# Let the user enter the key to use:
while True: # Keep asking until the user enters a valid key.
    max_key = len(SYMBOLS) - 1
    print(f"Please enter the key (0 to {max_key}) to use.")
    response: int = input("> ").upper()
    if not response.isdecimal():
        continue

    response = int(response)
    if 0 <= response < len(SYMBOLS):
        key: int = response
        break

# Let the user enter the message to encrypt/decrypt
print(f"Enter the message to {mode}")
message: str = input("> ")

# Caesar cipher only works on uppercase letters:
message = message.upper()

# Stores tthe encrypted/decrypted form of the message:
translated: str = ""

# Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # Get the encrypted (or decrypted) number for this symbol.
        num: int = SYMBOLS.find(symbol) # Get the number of the symbol.
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
        # Handle the wrap-around if num is larger than the length of 
        # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        # Juss add the symbol without encrypting/decrypting:
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)

pyperclip.copy(translated)
print(f"Full {mode}ed text copied to clipboard")




