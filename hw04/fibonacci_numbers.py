# Generates a list of numbers representing the first N Fibonacci sequence
# where N is the input value.

import sys


def main():
    # The Fibonacci sequence should begin with 0 and 1, initialize the
    # first and second num in Fibonacci sequence
    first_num = 0
    second_num = 1

    fibonacci_num = int(sys.argv[1])
    fibonacci_list = [first_num]
    fibonacci_range = fibonacci_num - 1

    # Each number after first and second num in the sequence should be the sum
    # of the two numbers before it.
    for _ in range(fibonacci_range):
        third_num = first_num + second_num
        first_num = second_num
        second_num = third_num
        fibonacci_list.append(first_num)

    print(fibonacci_list)


main()
