#!/usr/bin/python3
def roman_to_int(roman_string):
    sum = 0
    if type(roman_string) != str or not roman_string:
        return 0
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in reversed(roman_string):
        value = roman_numerals[i]
        sum += value if sum < value * 5 else -value
    return sum
