#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program finds greatest among numbers.

def main():

    # input
    first_number = int(input("Enter the first number : "))
    print("")
    second_number = int(input("Enter the second number : "))
    print("")

    # process
    if first_number > second_number:
        # output
        print("The greatest number is {}".format(first_number))
    elif first_number < second_number:
        print("The greatest number is {}".format(second_number))
    else:
        print("The numbers are same!")


if __name__ == "__main__":
    main()
