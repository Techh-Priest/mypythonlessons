#     Turtle Graphics
# from turtle import Turtle, Screen
# tim = Turtle()
#
# for _ in range(4):
#     tim.shape("turtle")
#     tim.color("red")
#     tim.forward(100)
#     tim.right(90)
import turtle
#Turtle Graphics relies on tkinter to create its graphics

#########################################################
        ## Importing Modules
# from turtle import * # the asterix is used to import everything from a particular module
#
# tim = Turtle()
# for _ in range(4):
#     tim.shape("turtle")
#     tim.color("red")
#     tim.forward(100)
#     tim.right(90)

        # Aliasing Modules
#import turtle as t # here we import turtle but give it a name that we define
# tim = t.Turtle()

# pypi is python's global library filled with libaries from all over the world.

#import heroes # Module has been installed from pypi
#print(heroes.gen())

########################################################
# from turtle import *
# import random
# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# for _ in range(50):
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)
#     tim.pd()

# colors = ["navy", "lime", "black", "red", "cyan", "green", "magenta", "brown", "maroon", "indigo", "olive drab", "yellow"]
#
# def draw_shape(num_of_sides):
#     for _ in range(num_of_sides):
#         angle = 360 / num_of_sides
#         tim.forward(100)
#         tim.right(angle)
#
#
# for side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(side)

##############################################################
# from turtle import *
# import random
# tim = Turtle()
#
# colors = ["navy", "lime", "black", "red", "cyan", "green", "magenta", "brown", "maroon", "indigo", "olive drab", "yellow"]
# directions = [0, 90, 180, 270]
# for _ in range(200):
#     tim.shape("turtle")
#     tim.width(5)
#     tim.color(random.choice(colors))
#     tim.speed(0)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

#################################################################

        # Tuples
#This is a data type in python.

#my_tuple = (1, 3, 8)
#print(my_tuple[0])

# A tuple doesn't support item reassigment or change it in amy way. It's immutable!!! e.g:
#my_tuple[2] = 11
#print(my_tuple)

# A tuple is really good for RGB color schemes
# If you want to edit anything in a tuple, convert it into a list first:
#print(list(my_tuple))

#####################################################3

# from turtle import *
# import random
# tim = Turtle()
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
# directions = [0, 90, 180, 270]
#
# for _ in range(200):
#     tim.shape("turtle")
#     tim.width(10)
#     tim.color(random_color())
#     tim.speed(0)
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


########################################################

# from turtle import *
# import random
# tim = Turtle()
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb = (r, g, b)
#     return rgb
#
# def spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.speed(0)
#         tim.width(2)
#         tim.setheading(tim.heading() + size_of_gap)
#         tim.circle(100)
#
# spirograph(3)

##################################################3

from turtle import *
import random
turtle.colormode(255)

# import colorgram
# colors = colorgram.extract('hirsty.jpg', 10)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# #remove colors close to white then create this list below

color_list = [(203, 34, 66), (0, 0, 0), (200, 54, 199), (255, 0, 0), (30, 249, 70), (160, 30, 180), (45, 233, 100), (71, 116, 151), (228, 161, 193), (150, 184, 70), (151, 160, 164), (242, 235, 46), (37, 161, 80)]
tim = Turtle()
tim.speed(0)
turtle.colormode(255)
tim.hideturtle()

def dotting():
    for dots in range(10):
        tim.penup()
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
        tim.pendown()


def turn():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)

    for dots in range(10):
        tim.forward(50)

    tim.right(90)
    tim.right(90)

tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for dots in range(10):
    dotting()
    turn()


screen = Screen()
screen.exitonclick()