def occurs(number, array):
    return True if array.count(number) else False

number = input("number: ")
array = input("Array: ").split()

print(f"Result: number {number} {'appears' if occurs(number,array) else 'does not appear'} in the array")

