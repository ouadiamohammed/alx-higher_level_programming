#!/usr/bin/python3

def safe_print_division(a, b):
    res = a / b
    try:
        return (res)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(res))
