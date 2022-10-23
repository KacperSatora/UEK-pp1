n = int(input("Enter the number: "))
flag = False

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break

if flag:
    print(f"Number {n} is not a prime number")
else:
    print(f"Number {n} is a prime number")

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
