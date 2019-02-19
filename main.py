import turtle
import random as ran
import math

turtle.hideturtle()
turtle.tracer(False)


def drawSquare():
    turtle.penup()
    turtle.goto(-250, -250)
    turtle.pendown()
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def drawCircle():
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.circle(250)
    gotocenter()


def gotocenter():
    turtle.penup()
    turtle.goto(0, 0)


def drawPoint(x, y):
    turtle.penup()
    #turtle.goto(-250+x,-250+y)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(2)
    turtle.penup()


drawSquare()
drawCircle()

inside = 0
total = 4000
for i in range(0, total):
    # Generate random x, y in [0, 1].
    x2 = ran.random()*2 -1
    y2 = ran.random()*2 -1
    turtle.goto(x2, y2)
    if(turtle.distance(0,0) <= 1.0):
        drawPoint(x2*250, y2*250)
        inside = inside + 1
        
pi = (float(inside) / total) * 4

print(pi)

turtle.exitonclick()