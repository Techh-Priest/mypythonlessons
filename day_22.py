import time
from paddle import *
from ball import *
from pong_score import *

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Andre's Pong")
screen.tracer(0)
screen.listen()


paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.ball_velocity)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Detect Collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 320 or ball.distance(paddle_2) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #Detect paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()












screen.exitonclick()