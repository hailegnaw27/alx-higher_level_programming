#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a is smaller than 2, add 0 for missing integers
    if len(tuple_a) < 2:
        tuple_a += (0, 0)

    # If tuple_b is smaller than 2, add 0 for missing integers
    if len(tuple_b) < 2:
        tuple_b += (0, 0)

    # Calculate the sum of the first elements and the sum of the second elements
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Return the resulting tuple
    return (sum_first, sum_second)

# Test the function with sample inputs
tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
