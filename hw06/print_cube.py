# prompts the user for a numerical value that is a multiple of 2
# and prints out a cube
# characters:
# + for cube corners, - for horizontal lines,
# | for vertical lines, and / for diagonals.
# for a cube of size n:
# 1) A horizontal edge is drawn with - and requires 2n characters.
# 2) A vertical edge is drawn with | and requires n characters.
# 3) A vertical edge is drawn with / and requires n/2 characters
# 4) Corners are drawn with +. Corners should line up with vertical
# and horizontal edges.


def main():
    size = cube_size()
    top_side(size)
    front_side(size)


# get the cube of size, if it is invalid input, ask the user to input again
def cube_size():
    size = (input("Input cube size (multiple of 2): "))
    while not size.isdigit():
        size = (input("Please input an integer." +
                " Input cube size (multiple of 2): "))

    while int(size) % 2 != 0:
        size = (input("Your input is not multiple of 2." +
                " Please input cube size (multiple of 2): "))

    size = int(size)
    return size


# print the top and part of side part of cube
def top_side(size):
    print(" " * (size // 2 + 1) + "+" + "-" * size * 2 + "+")
    for i in range(size + 1):
        if i <= size // 2 - 1:
            print(" " * (size // 2 - i) + "/" + " " * (size * 2) +
                  "/" + " " * i + "|")


# print the front and part of side part of cube
def front_side(size):
    for j in range((size + 2)//2):
        if j == 0:
            print("+" + "-" * size * 2 + "+" + " " * (size // 2) + "|")
        elif j <= size // 2 - 1:
            print("|" + " " * (size * 2) + "|" + " " * (size // 2) + "|")

    for k in range((size + 2)//2):
        if k == 0:
            print("|" + " " * (size * 2) + "|" + " " * (size // 2) + "+")
        elif k <= size // 2:
            print("|" + " " * (size * 2) + "|" + " " * (size // 2 - k) + "/")

    else:
        print("+" + "-" * size * 2 + "+")


main()
