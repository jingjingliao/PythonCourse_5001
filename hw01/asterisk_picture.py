# The function is to draw a tree
def draw_a_tree():
    for _ in range(3):
        for i in range(1, 5):
            print(" " * (4 - i), end="")
            print("*" * (2 * i - 1))

    for _ in range(4):
        print("   *   ")


draw_a_tree()
