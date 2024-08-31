

import turtle as t
import random

tim = t.Turtle()
tim.shape("circle")
tim.speed(0)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    my_color = (r, g, b)
    return my_color



screen = t.Screen()
def draw_many_circles(size_of_gap):
    circle_size_of_gape = int(360/size_of_gap)
    while size_of_gap>0:
        tim.color(random_color())
        current_heading = tim.heading()
        tim.circle(100)
        tim.setheading(current_heading+circle_size_of_gape)
        size_of_gap-=1
draw_many_circles(100)
screen.exitonclick()