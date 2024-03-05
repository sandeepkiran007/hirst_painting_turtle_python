import random
from turtle import Turtle, Screen
import turtle as t
t.colormode(255)
img_path = './painting.jpg'

colors = [(198, 13, 32), (248, 236, 25), (40, 76, 188),  (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]
x = -250
y = -250
tim = Turtle()
tim.penup()
for _ in range(10):
    tim.goto(x, y)
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    y += 50


screen = Screen()
screen.exitonclick()