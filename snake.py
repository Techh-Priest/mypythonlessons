from turtle import *
import time

STARTING_POS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for square in range(0, 3):
            body = Turtle()
            body.penup()
            body.shape("square")
            body.goto(x=STARTING_POS[square], y=0) # bug is here
            body.color("white")
            self.snake.append(body)
            #self.add_segment(square)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def add_segment(self, square):
        pass
        # body = Turtle()
        # body.penup()
        # body.shape("square")
        # body.goto(x=STARTING_POS[square], y=0) # bug is here
        # body.color("white")
        # self.snake.append(body)

    def extend(self):
        pass
#        self.add_segment(self.snake[-1].position()) # bug is here
