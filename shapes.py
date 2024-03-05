from turtle import Turtle, Screen

tim = Turtle()
tim.color('violet')
tim.pensize(4)
for s in range(3, 9):
    degree = 360 // s
    for i in range(s):
        tim.forward(50)
        tim.right(degree)


screen = Screen()
screen.exitonclick()