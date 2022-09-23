#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Sept 22 2022
# This program asks the user for the length and width of rectangle then calculates the area and perimeter of it


def main():
    # input
    length = int(input("Enter the length of the rectangle (mm): "))
    width = int(input("Enter the width of the rectangle (mm): "))
    # process
    area = length * width
    perimeter = 2 * (length + width)

    # output
    print("")
    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))


if __name__ == "__main__":
    main()
