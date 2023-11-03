#!/usr/bin/python3
"""
This is the "say_my_name" module.

This module supplies one function, say_my_name(first_name, last_name),
which prints the concatenation of the given first and last name.

Example:
    say_my_name("John", "Doe")

This will print:
    My name is John Doe.
"""

def say_my_name(first_name, last_name):
    """
    Print the concatenation of the given first and last name.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.

    Returns:
        None

    Raises:
        TypeError: If either argument is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe.

        >>> say_my_name("Jane", 123)
        Traceback (most recent call last):
            ...
        TypeError: last_name must be a string.

        >>> say_my_name(456, "Smith")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string.")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string.")

    print(f"My name is {first_name} {last_name}.")


if __name__ == "__main__":
    say_my_name("John", "Doe")
