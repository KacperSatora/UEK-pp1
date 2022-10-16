# Calculation of the area and circumference of a circle
import math

# determine radius and PI



pi = math.pi
radius = float(input("Enter the circle's radius:\n>"))

# calculate area 
area = pi * (radius**2)

# calculate circumference 
circumference = 2 * pi * radius

# display results 
print(f"Area is: {area}, and circumference is: {circumference}")
