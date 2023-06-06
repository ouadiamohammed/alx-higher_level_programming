#!/usr/bin/python3
for nbr1 in range(10):
    for nbr2 in range(nbr1 + 1, 10):
        print("{:d}{:d}".format(nbr1, nbr2), end="")
        if nbr1 < 8:
            print(", ", end="")
print()