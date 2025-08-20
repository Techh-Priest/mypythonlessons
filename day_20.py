#### Snake Game from Nokia 3310!!!

from turtle import Screen
import time
from snake import *
from food import *
from scoreboard import *


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("midnight blue")
screen.title("Andre's Snake Game")
screen.tracer(0)

anaconda = Snake()
food = Food()
scoreboard = ScoreBoard()


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
    # Detect Collision with food.
    if anaconda.head.distance(food) < 15:
        food.refresh()
        anaconda.extend()
        scoreboard.count_score()

    # Detect Collision with wall
    if anaconda.head.xcor() > 280 or anaconda.head.xcor() < -280 or anaconda.head.ycor() > 280 or anaconda.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect Collision with own Tail
    for snake in anaconda.snake[1:]:
        if anaconda.head.distance(snake) < 10:
            game_on = False
            scoreboard.game_over()


print(anaconda.extend())















screen.exitonclick()
