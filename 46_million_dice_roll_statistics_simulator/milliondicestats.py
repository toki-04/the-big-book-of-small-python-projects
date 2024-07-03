import random
import time

print('''Million Dice Roll Statistics Simulator
By Al Sweigart al@inventwithpython.com
Enter how many six-sided dice you want to roll:''')

number_of_dice = int(input("> "))

results = {}
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    results[i] = 0

print("Simulating 1,000,000 rolls of {} dice...".format(number_of_dice))
last_print_time = time.time()

for i in range(1000000):
    if time.time() > last_print_time + 1:
        print("{}% done...".format(round(i/10000, 1)))
        last_print_time = time.time()

    total = 0

    for j in range(number_of_dice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

print("TOTAL - ROLLS - PERCENTAGE")
for i in range(number_of_dice, (number_of_dice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print("  {} - {} rolls - {}%".format(i, roll, percentage))
