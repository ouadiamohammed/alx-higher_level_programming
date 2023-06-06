#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print(f"{number} is zero")
elif number < 0:
    print(f"{number} is negativ")
else:
    print(f"{number} is positiv")
