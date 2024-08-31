#####Turtle Intro######

import turtle as t
import random
# import heroes
# import villains
tim = t.Turtle()

# screen.onclick(turtle.goto)
tim.shape("circle")
tim.color("orange")

tim.speed(0)
tim.pensize(15)
# tim.pen(fillcolor = random.choice(my_colours), pencolor =  random.choice(my_colours), pensize = 15)
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    my_color = (r, g, b)
    return my_color

def direction_angle_choose():
    tim.color(random_color())
    return tim.setheading(random.choice(range(0, 271, 90)))

def direction_move_choose(x):
    return tim.forward(x)


user_ask_walk = int(input('how many random walk you want to do?: '))
user_ask_steps = int(input('how many random steps you want to do?: '))
while user_ask_walk>0:
    direction_angle_choose()
    direction_move_choose(user_ask_steps)
    user_ask_walk-=1