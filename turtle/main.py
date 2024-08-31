#####Turtle Intro######

import turtle as t
import random
# import heroes
# import villains
tim = t.Turtle()
gio = t.Turtle()
gio.penup()
gio.setpos(200, 50)
gio.pendown()
# screen.onclick(turtle.goto)
tim.shape("circle")
tim.color("orange")
gio.shape("turtle")
gio.color("black")
my_colours = ["medium purple", "lime green", "deep pink", "coral", "midnight blue", "medium spring green"]
def draw_shapes(side, my_object):
    '''it will take the number of sides and the object, will result in different shapes'''
    sides = 360/side
    for x in range(side):
        my_object.right(sides)
        my_object.forward(100)
for x in range(3, 8):
    tim.color(random.choice(my_colours))
    draw_shapes(x, tim)
    gio.color(random.choice(my_colours))
    draw_shapes(x, gio)
tim.setpos(-90,30)
for x in range(5):
    tim.color(random.choice(my_colours))
    tim.right(144)
    tim.forward(200)

tim.done()
# will draw a star

######## Challenge 1 - Draw a Square ############

