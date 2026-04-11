#!/usr/bin/python3

def fizzbuzz():
    """Prints numbers 1 to 100 with Fizz, Buzz, and FizzBuzz logic."""
    for i in range(1, 101):
        # Check if number is multiple of both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end="")
        # Check if number is multiple of 3
        elif i % 3 == 0:
            print("Fizz", end="")
        # Check if number is multiple of 5
        elif i % 5 == 0:
            print("Buzz", end="")
        # Otherwise, print the number itself
        else:
            print("{}".format(i), end="")
        
        # Always print a space after each element
        print(" ", end="")
