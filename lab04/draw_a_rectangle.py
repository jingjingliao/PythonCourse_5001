# make a rectangle based on user's input for rectangle’s symbol, width
# and height

MINIMUM_SIZE = 2


# make sure user's inputs are valid, the input can not be lower than 2
def user_input(boundary_name):
    length = int(input("Please input an integer (no less than 2)" +
                       " as rectangle's " + boundary_name + ": "))
    while (length < MINIMUM_SIZE):
        print("The " + boundary_name + " value should not be lower than 2")
        length = int(input("Please input an integer (no less than 2)" +
                           " as rectangle's " + boundary_name + ": "))

    return length


# ask the user to input a symbol and create a rectangle
# the first and last row have symbols with the number of width value
# the middle width has just one symbol in the first and last column
def main():
    symbol = input("Please input any single character: ")
    width = user_input('width')
    height = user_input('height')
    middle_width = width - 2
    for index in range(height):
        if (index == 0 or index == height-1):
            print(symbol * width)
        else:
            print(symbol + " " * (middle_width) + symbol)


main()
