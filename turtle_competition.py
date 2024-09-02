from turtle import Turtle, Screen

import random

game_is_on = False
screen = Screen()
print(screen.getshapes())
screen.setup(width = 500, height = 400)
player_bet = screen.textinput(title = 'Make your bet', prompt = 'Which turtle will win the race? Enter a color: ')
print(player_bet)
colors = ['red', 'green', 'yellow', 'orange', 'blue', 'purple']
yaxis_pos = [100, 50, 0, -50, -100, -150]




turtle_list = []

for turtle_color in colors:
    new_turtle = Turtle(shape = 'turtle')
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.goto(x = -240,y = yaxis_pos[colors.index(turtle_color)])
    turtle_list.append(new_turtle)


# creating a finish line
finish_line = Turtle(shape = 'blank')
finish_line.speed("fastest") 
finish_line.penup()
finish_line.setpos(x=230, y = 130)
finish_line.stamp()
finish_line.pendown()
finish_line.setheading(-90)
finish_line.forward(300)

finish_line.penup()
# setting a position a flag
finish_line.goto(x = -240, y = 135)


def flag():
    """will create a flag"""
    finish_line.setheading(80)
    finish_line.pendown()
    finish_line.forward(50)
    finish_line.right(120)
    finish_line.color("black", "blue")
    finish_line.begin_fill()
    finish_line.forward(30)
    finish_line.left(180 - finish_line.heading())
    finish_line.forward(28)
    finish_line.end_fill()


while finish_line.xcor()<230:
    # will create a number of blue flags
    flag()
    finish_line.penup()
    finish_line.setheading(0)
    finish_line.goto(x =  finish_line.xcor()+50, y = 135)
    finish_line.setheading(90)
    finish_line.pendown()


screen.update()
if player_bet:
    game_is_on = True

while game_is_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            game_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == player_bet:
                print(f"You won, {winning_color} is the winner:)")
            else:
                print(f"You lost, {winning_color} is the winner:(")
            break
        turtle_distance_random = random.randint(0,10)
        turtle.forward(turtle_distance_random)
screen.exitonclick()