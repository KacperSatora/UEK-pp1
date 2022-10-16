import random

number = random.randint(1,6)

guess = int(input("Guess the number:\n>"))

if guess == number:
    print("You win!")
else:
    print(f"Wrong answer, the number was {number}")