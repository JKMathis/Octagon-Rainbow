#!/usr/bin/env python3.10

import turtle

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'turquoise', 'skyblue', 'grey', 'black']

#create turtle object variable

djr = turtle.Turtle()
djr.shape('turtle')
djr.width(8)
djr.penup()
djr.setpos(-50, 50)
djr.pendown()

#looping to rainbow list to create Octagon

for side in rainbow:
    djr.color(side)
    djr.forward(100)
    djr.right(45)
djr.hideturtle()

draw = turtle.Turtle()
rainbow = ['blue', 'purple', 'green', 'yellow', 'orange', 'red', 'turquoise', 'pink']
draw.speed(2)
draw.width(5)
draw.setpos((-25, 25))

for side in rainbow:
    draw.color(side)
    draw.forward(50)
    draw.right(135)
draw.hideturtle()


