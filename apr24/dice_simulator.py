import random

while True:
    print("Dice:", random.randint(1,6))
    if input("Roll again? (y/n): ") == 'n':
        break