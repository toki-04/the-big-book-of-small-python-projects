print("Caesar Cipher Hacker, by A; Sweigart al@inventwithpython.com")
message: str = input("> ")

# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message to hack.)
SYMBOLS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(SYMBOLS)): 
    translated: str = ""

    # Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num: int = SYMBOLS.find(symbol) # Get the number of the symbol
            num = num - key # Decrypt the  number

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num+ len(SYMBOLS)

            # Add decrypted number's sysmbol to be translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting
            translated = translated + symbol

    # Dsiplay the key being tested, along with its decrypted text:
    print(f"Key #{key}: {translated}")

