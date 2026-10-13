#!/usr/bin/env python3

# Created by: Mignonne Gihozo
# Created on: Oct 2026
# Modified by: Ms Raffin
# Modified on: Oct 13, 2026
# This program calculates the area and perimeter of a semicircle based on the radius provided by the user.

import math


def main():
    # display the initial greeting to the user
    print("Welcome to the Semicircle Calculator program!")
    print("")

    # get the radius from the user
    radius = int(input("Enter the radius of the semicircle: "))
    print("")

    # process: calculate diameter, area, and perimeter
    diameter = radius * 2
    area = (math.pi * (radius**2)) / 2
    perimeter = (math.pi * (diameter / 2)) + diameter

   
    # output: display the results to the user
    print("--- Results ---")
    print(f"Area of the semicircle: {area:.2f}")
    print(f"Perimeter of the semicircle: {perimeter:.2f}")


if __name__ == "__main__":
    main()
