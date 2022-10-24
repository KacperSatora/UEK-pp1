import mymath

while True:
    guess = mymath.read_number()
    number = mymath.generate_number()
    if guess == number:
        print("Correct")
        break
    else:
        print(f"The number was {number}, your guess - {guess}\nTry again")