from turtle import Turtle
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class SnakeMove:
    def __init__(self):
        self.turtle_list = []
        self.initial_snake()
        self.front = self.turtle_list[0]

    def initial_snake(self):
        for turtles in INITIAL_POSITIONS:
            self.add_snake(turtles)

    def add_snake(self, turtles):
        t = Turtle("square")
        t.color("brown")
        t.penup()
        t.goto(turtles)
        self.turtle_list.append(t)

    def grow_snake(self):
        self.add_snake(self.turtle_list[-1].position())

    def snake_move(self):
        for t in range(len(self.turtle_list) - 1, 0, -1):
            x = self.turtle_list[t - 1].xcor()
            y = self.turtle_list[t - 1].ycor()
            self.turtle_list[t].goto(x, y)
        self.front.forward(MOVING_DISTANCE)

    """functions to move the snake up,down, left and right"""
    def snake_up(self):
        if self.front.heading != DOWN:
            self.front.setheading(UP)


    def snake_down(self):
        if self.front.heading != UP:
            self.front.setheading(DOWN)


    def snake_left(self):
        if self.front.heading != RIGHT:
            self.front.setheading(LEFT)


    def snake_right(self):
        if self.front.heading != LEFT:
            self.front.setheading(RIGHT)

