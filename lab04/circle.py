# takes a value from the command line and prints out a circle with the radius
# corresponding to that value.

import sys
import math


def main():
    radius = int(sys.argv[1])
    diameter = radius * 2

    # create a grid containing letter "o", which is twice the
    # radius high and twice the radius wide.

    list1 = []
    for _ in range(diameter):
        string1 = "o" * diameter
        list1.append(list(string1))

    # find each character's position in terms of an i and j position
    # in the list. Determine whether the distance of each character
    # to the center of the grid is less than the value of the radius_distance.
    # If the distance is less than the radius_distance, then the o character
    # will be rendered in that position, otherwise the (empty space)
    # will be rendered in that position.

    center_position = radius - 1
    radius_distance = (diameter - 1)/2

    for i in range(diameter):
        for j in range(diameter):
            if int((math.sqrt((i - center_position) ** 2 +
               (j - center_position) ** 2))) > radius_distance:
                list1[i][j] = " "

    # convert the grid list into a string
    for each in list1:
        print("".join(each))

main()
