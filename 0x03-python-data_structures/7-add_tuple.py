#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they are smaller than 2 elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Add the first elements of each tuple
    sum_1 = tuple_a[0] + tuple_b[0]

    # Add the second elements of each tuple
    sum_2 = tuple_a[1] + tuple_b[1]

    # Return a new tuple with the sums
    return (sum_1, sum_2)

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))
