#!/usr/bin/env python3
""""
Created by: Nina Mathew
Created on: April 17, 2023
This is the " value of one number raised to the power of another. " module
"""


def main() -> None:
    """The main() this function uses a while loop, returns None."""
    # Write a program to find the value of one number raised to the power of another.
    # Do not use any built-in method, you must use a loop.
    # Ask the user for the number to be raised to the power.
    # With try and except statements, you can handle exceptions.

    # Input
    print("This program finds the value of one number raised to the power of another.")
    print("")
    base_str = input("Enter the base number: ")
    exponent_str = input("Enter the exponent number: ")
    print("")
    # Process & Output
    # With try and except statements, that catch strings that cannot be converted to integer.
    try:
        base_int = int(base_str)
        exponent_int = int(exponent_str)
        answer = 1
        while exponent_int >= 0:
            answer = answer * base_int
            exponent_int = exponent_int - 1
        print(f"The answer is: {answer}")
    except ValueError:
        print("Invalid input, try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
