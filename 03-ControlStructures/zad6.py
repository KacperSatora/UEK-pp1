import random

carSpeed = random.randint(0,280)

print("Car exceeded the speed limit") if carSpeed > 130 else print("Car speed is below the limit")

# if carSpeed > 130:
#     print(f"Car exceeded the speed limit {carSpeed}")
# else:
#     print(f"Car speed is below the limit {carSpeed}")