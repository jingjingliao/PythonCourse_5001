# draws a diamond out of asterisks, takes an int argument representing
# the height of the diamond and prints out an appropriately-sized diamond.

import sys


# get the value of height and calculate the middle height of the diamond
def main():
    height = int(sys.argv[1])
    middle_height = height // 2

    # if height is an odd value, the number of widest asterisks is the number
    # of height, if height is an even value, the number of widest is height - 1
    if height % 2 == 0:
        maximum_width_asterisks = height - 1
    else:
        maximum_width_asterisks = height

    # print the higher half of the diamond using mathmatical way
    for i in range(middle_height):
        if height % 2 != 0:
            print(" " * (middle_height - i) + "*" * (2 * i + 1))
        else:
            print(" " * (middle_height - i - 1) + "*" * (2 * i + 1))

    # print the lower half of the diamond using mathmatical way
    for j in range(height - middle_height):
        print(" " * j + "*" * (maximum_width_asterisks - 2 * j))


main()
