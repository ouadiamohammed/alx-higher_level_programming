#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
        return res
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
