from turtle import Turtle, Screen
import random as r

turtle = Turtle()
turtle.shape("turtle")

screen = Screen()
screen.colormode(255)
## Each turn needs to be the number of sides / 360
## Keep track of number of sides drawn

def calculate_angle(x):
    return 360 / x


def draw_line(x):
    """ Move turtle 100 paces and turn depending on input of x"""
    turtle.forward(100)
    turtle.right(x)

def check_origin(sides_to_draw, drawn_sides):
    """ Return False if all sides aren't drawn, otherwise return True"""
    if drawn_sides < sides_to_draw:
        return False
    return True

def randomize_colors():
    color_list = []
    for _ in range(3):
        color = r.randint(0, 255)
        color_list.append(color)
    return color_list


for _ in range (3, 11):
    # Iterate through number of sides of shape
    sides = 0 # Keep track of number of sides to draw
    angle = calculate_angle(_)
    colors = tuple(randomize_colors())
    turtle.pencolor(colors[0], colors[1], colors[2])
    while not check_origin(_, sides):
        draw_line(angle)
        sides += 1


















screen.exitonclick()