
from turtle import Turtle, Screen
import turtle as t
import random
tim = Turtle()
t.colormode(255)
turtle_direction = [tim.right, tim.left]
turtle_degrees = [90, 180, 270, 360]
moves = [tim.forward, tim.backward]
tim.pensize(12)
tim.speed(0)


def random_move():
    return random.choice(moves)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



def random_direction():
    return random.choice(turtle_direction)


def random_degree():
    return random.choice(turtle_degrees)




for _ in range(3000):
    tim.pencolor(random_color())
    random_direction()(random_degree())
    random_move()(25)



screen = Screen()
screen.exitonclick()