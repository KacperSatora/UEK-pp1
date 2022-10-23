amount = int(input("Enter the amount in PLN: "))
coin5 = amount // 5
amount -= coin5 * 5
coin2 = amount // 2
amount -= coin2 * 2
coin1 = amount // 1
amount -= coin1
print(f"5zl - {coin5}\n2zl - {coin2}\n1zl - {coin1}")
    
