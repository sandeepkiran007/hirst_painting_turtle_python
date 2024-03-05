from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = Turtle()
tim.pensize(2)
tim.speed('fastest')
for _ in range(360):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.left(10)


screen = Screen()
screen.exitonclick()