from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.seg_head.distance(food) < 15:
        snake.extend_snake()
        food.refresh()
        scoreboard.score_increase()

    if (snake.seg_head.xcor() > 280 or snake.seg_head.xcor() < -280
            or snake.seg_head.ycor() > 280 or snake.seg_head.ycor() < -280):
        # game_on = False
        # scoreboard.game_over_dashboard()
        scoreboard.reset_game()
        snake.snake_reset()

    # tail detect
    for segment in snake.segments[1:]:
        if segment == snake.segments:
            pass
        elif snake.seg_head.distance(segment) < 10 :
            scoreboard.reset_game()
            snake.snake_reset()
            # game_on = False
            # scoreboard.game_over_dashboard()

screen.exitonclick()
