import turtle
import random as ran





def drawSquare():
    turtle.penup()
    turtle.goto(-350, -350)
    turtle.pendown()
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


def drawCircle():
    turtle.penup()
    turtle.goto(0, -350)
    turtle.pendown()
    turtle.circle(350)
    gotocenter()


def gotocenter():
    turtle.penup()
    turtle.goto(0, 0)


def drawPoint(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(2)
    turtle.penup()


total = int(input("Number of iterations"))

turtle.hideturtle()
turtle.tracer(False)
drawSquare()
drawCircle()

inside = 0

for i in range(0, total):
    # Generate random x, y in [0, 1].
    x2 = ran.random() * 2 - 1
    y2 = ran.random() * 2 - 1
    turtle.goto(x2, y2)
    if(turtle.distance(0, 0) <= 1.0):
        drawPoint(x2 * 350, y2 * 350)
        inside = inside + 1
pi = (float(inside) / total) * 4

print(pi)

turtle.exitonclick()
