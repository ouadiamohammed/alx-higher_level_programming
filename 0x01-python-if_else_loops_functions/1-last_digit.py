#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    modulo = ((number * -1) % 10) * -1

else:
    modulo = number % 10

str = "last digit of {:d} is {:d} and is"
if modulo == 0:
    print(str.format(number, modulo) + " 0")
elif modulo > 5:
    print(str.format(number, modulo) + " greater than 5")
else:
    print(str.format(number, modulo) + " less than 6 and not 0")
