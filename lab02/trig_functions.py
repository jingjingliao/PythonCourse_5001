import math


def main():
    angle = float(input("Enter an angle: "))
    radian = math.radians(angle)
    cosine_of_angle = math.cos(radian)
    sin_of_angle = math.sin(radian)
    print("The cosine of {} is {}".format(angle, cosine_of_angle))
    print("The sine of {} is {}".format(angle, sin_of_angle))


main()
