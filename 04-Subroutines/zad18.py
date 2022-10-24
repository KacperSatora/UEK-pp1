def sumOfDigits(n):
    sum = 0
    for num in n:
        sum += int(num)
    return sum

print(sumOfDigits("7182"))
