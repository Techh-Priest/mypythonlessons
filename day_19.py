#import turtle  # More on Turtle Graphics, Eventlisteners, Higher Order Functions, State & Multiple Instances of an Object

# from turtle import *
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# screen.listen()
# screen.onkey(key="space", fun=move_forwards) # When you use a function as an argument, you don't add
#         # the parantheses at the end because we don't want to trigger the function at this point. We want it to
#         # be triggered when the space bar is pressed/ or when the event being listened for occurs.
# screen.exitonclick()

# A higher order function is a function that takes another function as an input/argument.
# this is important when we need to listen for events and then trigger a functions

#################################################################################

    # Etch-A-Sketch Program
# from turtle import *
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def clockwise():
#     tim.left(25)
#
# def anti_clockwise():
#     tim.right(25)
#
# def wipe_screen():
#     tim.penup()
#     tim.clear()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="a", fun=anti_clockwise)
# screen.onkey(key= "c", fun=wipe_screen)
# screen.exitonclick()

#########################################################
from turtle import *
import random
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor("midnight blue")

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "pink", "purple", "cyan"]
y_position = [-70, -40, -10, 20, 50, 80]
racers = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(0)
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    racers.append(new_turtle)

race_on = False

if user_bet:
    race_on = True

while race_on:

    for racer in racers:
        if racer.xcor() > 230:
            race_on = False
            winner = racer,pencolor()
            if winner == user_bet:
                print(f"You won! The {winner} turtle is the winner.")
            else:
                print(f"You lost. The {winner} turtle is the winner")

        random_pace = random.randint(0, 10)
        racer.forward(random_pace)


screen.exitonclick()