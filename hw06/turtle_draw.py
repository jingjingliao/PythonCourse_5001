# This program is to use turtle module to draw the star with red outline and
# yellow filled arms and the circle with blue outline and cyan fill
import turtle
import math

STAR_LENGTH = 500
STAR_DEGREE = 72


def main():
    radius = get_radius()
    draw_circle(radius)
    draw_star()


# Calculate the radius of the circle
def get_radius():
    HALF_STAR_LENGTH = STAR_LENGTH // 2
    radius = HALF_STAR_LENGTH / math.sin(math.radians(STAR_DEGREE))
    return radius


# Draw the circle with blue outline and cyan fill
def draw_circle(radius):
    CIRCLE_DEGREE = 360
    CIRCLE_FORWARD_ANGLE = 1

    # set the color and put the pen in the right position
    turtle.begin_fill()
    turtle.color("blue", "cyan")
    turtle.penup()
    turtle.setposition(0, radius)
    turtle.pendown()

    for _ in range(CIRCLE_DEGREE):
        circle_perimeter = 2 * math.pi * radius
        turtle.forward(circle_perimeter / CIRCLE_DEGREE)
        turtle.right(CIRCLE_FORWARD_ANGLE)

    turtle.end_fill()


# Draw the star with red outline and yellow fill
def draw_star():
    STAR_ANGLE = 5
    STAR_FORWARD_ANGLE = 144

    turtle.begin_fill()
    turtle.color("red", "yellow")
    turtle.right(STAR_DEGREE)

    for _ in range(STAR_ANGLE):
        turtle.forward(STAR_LENGTH)
        turtle.right(STAR_FORWARD_ANGLE)

    turtle.end_fill()
    turtle.done()


main()
