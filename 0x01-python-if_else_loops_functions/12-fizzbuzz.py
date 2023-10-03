#!/usr/bin/python3

def fizzbuzz():
    """
    Prints the numbers from 1 to 100, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
