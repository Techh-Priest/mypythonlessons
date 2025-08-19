        #### Snake Game from Nokia 3310!!!

from turtle import *
import time
from snake import *

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("midnight blue")
screen.title("Andre's Snake Game")
screen.tracer(0)

anaconda = Snake()
screen.listen()
screen.onkey(anaconda.up, "Up")
screen.onkey(anaconda.down, "Down")
screen.onkey(anaconda.left, "Left")
screen.onkey(anaconda.right, "Right")



game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)

    anaconda.move()

















screen.exitonclick()