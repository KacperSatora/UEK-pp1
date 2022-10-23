codePin = "0805"
for i in range(3):
    x = input("Enter the PIN code: ")
    if x == codePin:
        print("Match")
        break
    else:
        print("Incorrect...")
else:
    print("Payment declined, card has been blocked")