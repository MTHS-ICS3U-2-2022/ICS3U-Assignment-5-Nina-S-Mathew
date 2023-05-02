#!/usr/bin/env python3
""""
Created by: Nina Mathew
Created on: April 17, 2023
This is the " value of one number raised to the power of another. " module
"""


def main() -> None:
    """The main() this function uses a while loop, returns None."""
    answer = 1

    # input
    base_number_str = input("Enter the number of which you have to find power: ")
    power_number_str = input("Enter the power: ")
    print("")

    # process & output
    try:
        base_number = int(base_number_str)
        power_number = int(power_number_str)
    except ValueError:
        print("Invalid, Input. Please try again.")
    if power_number < 0:
        print("Invalid, Input. Please try again.")
    else:
        for base_number in range (power_number + 1):
            answer = base_number * answer
            print(f"The power of {base_number} by {power_number} is {answer}.")
            break
    print("\nDone.")


if __name__ == "__main__":
    main()
