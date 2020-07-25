# The function is to print out the "triangular number" of the input number
# A triangular number counts objects arranged in an equilateral triangle.
# The nth triangular number is the number of dots in the triangular arrangement
# with n dots on a side, and is equal to the sum of the n natural numbers
# from 1 to n.

import sys


ADD_NUM = 1
DIVIDE_NUM = 2


def main():
    input_num = int(sys.argv[1])
    triangular_num = int((input_num * (input_num + ADD_NUM)) / DIVIDE_NUM)

    print("The triangular number of your input number", input_num, "is",
          triangular_num)


main()
