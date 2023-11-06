#!/usr/bin/python3
okup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-lookup.txt")
