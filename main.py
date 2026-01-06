from turtle import Turtle, Screen
import random as r

turtle = Turtle()
turtle.hideturtle()
# turtle.pen(resizemode="auto")
# turtle.shape("circle")
# turtle.resizemode("auto")
turtle.speed("fastest")
turtle.degrees()
screen = Screen()
screen.colormode(255)
## Each turn needs to be the number of sides / 360
## Keep track of number of sides drawn

def randomize_colors():
    red = r.randint(0,255)
    green = r.randint(0, 255)
    blue = r.randint(0, 255)
    return (red, green, blue)

def draw_spirograph(degrees):
    full_circle = 360
    degrees_turned = 0
    while full_circle >= degrees_turned:
        turtle.color(randomize_colors())
        turtle.circle(100)
        turtle.left(degrees)
        degrees_turned += degrees

draw_spirograph(10)
screen.exitonclick()


















