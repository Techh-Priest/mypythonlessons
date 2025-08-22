from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("magenta")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()