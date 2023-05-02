#!/usr/bin/env python3
""""
Created by: Nina Mathew
Created on: April 17, 2023
This is the " value of one number raised to the power of another. " module
"""


def main() -> None:
    """The main() this function uses a while loop, returns None."""
    base_number = 0
    power_number = 0
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
        for power_number_str in range(power_number):
            answer = base_number**power_number
            print(f"The power of {base_number} by {power_number} is {answer}.")
            break
    print("\nDone.")


if __name__ == "__main__":
    main()
