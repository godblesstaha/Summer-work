#DiceRoll
import random

choice = input("Do you want to roll the dice? (y/n): ")
while choice != "y" and choice != "n":
    print("Your choice is invalid!")
    choice = input("Do you want to roll the dice? (y/n): ")

while choice == "y":
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    print(f"You rolled: ({x}, {y})")
    choice = input("Do you want to roll again? (y/n): ")

    while choice != "y" and choice != "n":
        print("Your choice is invalid!")
        choice = input("Do you want to roll again? (y/n): ")

print("Thanks for playing the game!")