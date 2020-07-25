# This program is to prints out a rocket consisting of a nose cone, a fuselage,
# and a tail fin structure.


import sys


# if user's input is valid, execute the following function, if not, let the
# user know that the input is invalid
def main():
    try:
        width, square, is_striped = user_input()
        nose_cone_configuration(width)
        segment_structure(width, square, is_striped)
        tail_configuration(width)
    except Exception as error:
        print(error)


# check whether the user's input is valid, if it is valid, return input value
def user_input():
    if sys.argv[1].isdigit() is True and sys.argv[2].isdigit() is True:
        width = int(sys.argv[1])
        square = int(sys.argv[2])
    else:
        raise Exception("Your input is invalid, please input integer number")

    is_striped = False
    if len(sys.argv) == 4:
        if sys.argv[3] == 'striped':
            is_striped = True
        else:
            raise Exception("Your third input is invalid,"
                            " please input 'striped' as third input")

    return width, square, is_striped


# print the nose cone part, considering about whether the width is odd or even
def nose_cone_configuration(width):
    half_width = width // 2
    for i in range(half_width):
        if width % 2 != 0:
            print(" " * (half_width - i) + "*" * (2 * i + 1))
        else:
            print(" " * (half_width - i) + "*" * (2 * i))


# if user input striped as the third input, use "_" for segment part. Otherwise
# use "X"
def segment_structure(width, square, is_striped):
    half_width = width // 2
    for j in range(square):
        for k1 in range(width // 2):
            if (is_striped):
                print("_" * width)
            else:
                print("X" * width)
        for k2 in range(width - width // 2):
            print("X" * width)


# firstly, tell whether the width is odd or even, if it is odd and remainder is
# even when mod 2, then half_width should be odd (width // 2 + 1), if it is not
# half width is width // 2
def tail_configuration(width):
    if width % 2 != 0 and (width // 2) % 2 == 0:
        half_width = width // 2 + 1
    elif width % 2 == 0 and (width // 2) % 2 != 0:
        half_width = width // 2 + 1
    else:
        half_width = width // 2

    while half_width <= width:
        print(" " * ((width - half_width) // 2) + "*" * half_width)
        half_width += 2

    print("*" * width)


main()
