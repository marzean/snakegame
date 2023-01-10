from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Yellow")
        self.hideturtle()
        self.penup()
        self.goto(-50, 270)
        self.increase_score()

    def increase_score(self):
        self.write(f"Your Score:{self.score}", font=("Verdana", 10, "normal"))

    def control_score(self):
        self.score += 1
        self.clear()
        self.increase_score()

    def game_over(self):
        self.goto(-50, 0)
        self.write(f"Game Over!", font=("Verdana", 10, "normal"))

