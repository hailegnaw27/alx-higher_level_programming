#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None


if __name__ == "__main__":
    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div:", result)

    result = safe_function(my_div, 10, 0)
    print("result of my_div:", result)

    def print_list(my_list, length):
        i = 0
        while i < length:
            print(my_list[i])
            i += 1
        return length

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list:", result)
