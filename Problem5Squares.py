#Syed Hussain
#08/20/2022
#Problem number 5 - Using the following given chunk of code as a base to produce the image.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

alex = turtle.Turtle()
alex.pensize(2)
alex.speed(10)
alex.color('blue')
space = -10

for i in range(20, 105, 20):
        drawSquare(alex,i)
        alex.up()
        alex.goto(space, space)
        alex.down()
        space = space - 10

wn = turtle.Screen()
wn.exitonclick()


