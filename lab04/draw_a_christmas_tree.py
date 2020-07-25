# draw a christmas tree. The left edge of the tree is made up of / characters
# and the right edge is made up of \ characters,
# the base (between the two edge characters)is made up of underscores (_),
# and the top of the tree is an asterisk. The height of a tree should be no
# less than MINIMUM_VALUE 3


MINIMUM_VALUE = 3


# ask the user to give an input value, which can determin the height of
# a tree
def height(input_value):
    input_value = int(input("Please input an odd-valued no less than 3:  "))

    # when the value is even or less than 3, ask the user to input again
    while(input_value % 2 == 0 or input_value < MINIMUM_VALUE):
        if input_value % 2 == 0:
            print("Your input value is an even number")
            input_value = int(input("Please input an odd-valued" +
                                    " no less than 3:  "))
        if input_value < MINIMUM_VALUE:
            print("Your input value is less than 3")
            input_value = int(input("Please input an odd-valued" +
                                    " no less than 3:  "))

    return input_value


# print the tree, the top of the tree is an asterisk, the left and right
# side is "/" and "\" character, the edge is made up with "_"
# range_height is the height without top and edge. edge_distance stands
# for how many "_" for edge, the space between "/" and "\" is (2 * index + 1)
def main():
    input_value = int(height("input_value"))
    tree_height = input_value // 2

    range_height = tree_height - 1
    edge_distance = input_value - 2

    print(" " * tree_height + "*")
    for index in range(tree_height):
        if (index == tree_height - 1):
            print("/" + "_" * (edge_distance) + "\\")
        else:
            print(" " * (range_height - index) + "/" +
                  " " * (2 * index + 1) + "\\")


main()
