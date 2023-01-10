from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.new_location()

    def new_location(self):
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)
