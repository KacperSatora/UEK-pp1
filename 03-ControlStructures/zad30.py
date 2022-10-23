import math


n = int(input("Enter the number: "))


def pF(n):
    while n % 2 == 0:
        print(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            print(i)
            n = n / 1
    if n > 2:
        print(n)

pF(n)


# for i in range(2, n):
#     if n % i == 0:
#         print("NOT PRIME")
#         break
#     else:
#         print("The number is a prime number")
#         break
# primes = [2]
# for i in range(2,n + 1):
#     for j in range(2, i):
#         print(f"{i}/{j}")
#         if i % j == 0:
#             print("DIVISOR FOUND")
#             primes.pop()
#             break
#         else:
#             primes.append(i)
# print(primes)
# primes = list(set(primes))
# print(primes)
