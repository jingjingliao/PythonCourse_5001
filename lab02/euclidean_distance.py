import math

"""
Input four numerical values representing two 2-dimensional points,
calculates the Euclidean distance between the two points
"""


def main():

    num_x1 = float(input("Enter a numeric value x1: "))
    num_y1 = float(input("Enter a numeric value y1: "))
    num_x2 = float(input("Enter a numeric value x2: "))
    num_y2 = float(input("Enter a numeric value y2: "))

    square_distance_x_and_y = (num_y2 - num_y1) ** 2 + (num_x2 - num_x1) ** 2
    euclidean_distance = math.sqrt(square_distance_x_and_y)

    print(("The Euclidean distance between {} and {} is {:.2f}".format((num_x1, num_y1), (num_x2, num_y2), euclidean_distance)))


main()
