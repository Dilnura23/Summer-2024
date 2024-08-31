import math
from turtle import *

tim = Turtle()
screen = Screen()
def heart(k):
    return 15*math.sin(k)**3

def heart1(k):
    return 12*math.cos(k)-5*\
        math.cos(2 * k) - 2* \
        math.cos(3 * k)-\
        math.cos(4 * k)

tim.speed(1000)

screen.bgcolor("black")
for i in range(6000):
    tim.setpos(heart(i)*20, heart1(i)*20)
    for j in range(5):
        tim.color("pink")

tim.done()