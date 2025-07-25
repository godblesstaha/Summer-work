# guess the number
import random

number = random.randint(1,100)

while True:
    guess_input=input("Guess the number between 1and 100: ")
    if guess_input.isdigit():
        guess=int(guess_input)

        if guess > number:
            print("Too high")

        if guess < number:
            print("Too low")

        if guess == number:
            print("Congrats you found the number")
            break
    else:
        print("Please enter a valid number")