import time
from turtle import Screen
from food import Food
from snakemove import SnakeMove
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to snake game!")


game_on = True
screen.tracer(0)
screen.bgcolor("coral")

snake = SnakeMove()
food = Food()
score = Score()
"""Listening to keys and move the snake different direction"""
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    """if the snake eat the food it will take the food to a new location"""
    if snake.front.distance(food) < 20:
        food.new_location()
        snake.grow_snake()
        score.control_score()
    """if the snake hit a wall game will end"""
    if snake.front.xcor() > 280 or snake.front.xcor() < -280 or snake.front.ycor() > 290 or snake.front.ycor() < -290:
        score.game_over()
        game_on = False
    """this part will check if the snake hits it tails"""
    for turtles in snake.turtle_list[1:]:
        if snake.front.distance(turtles) < 10:
            game_on = False
            score.game_over()





















screen.exitonclick()
