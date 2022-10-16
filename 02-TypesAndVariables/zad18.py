from math import sqrt


a = float(input("Set a: "))
b = float(input("Set b: "))
c = float(input("Set c: "))
 
p = (a + b + c) / 2

area = sqrt(p * (p - a) * (p - b) * (p - c))
print(area)
