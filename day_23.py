import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from turtle_crossing_score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("indigo")
screen.tracer(0)

tortoise = Player()
screen.listen()
screen.onkey(tortoise.move, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_score()

    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(tortoise) < 42:
            game_on = False
            scoreboard.game_over()

    # Detect tortoise has crossed successfully
    if tortoise.finish_line():
        tortoise.start_over()
        car_manager.next_level()
        scoreboard.increase_level()


screen.exitonclick()
