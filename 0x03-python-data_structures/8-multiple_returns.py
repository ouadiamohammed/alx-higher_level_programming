#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = () + (0, "")
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    tuple = (len(sentence), first_char)
    return tuple
