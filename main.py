from turtle import Turtle,Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

turtle=Turtle()
screen=Screen()
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.setup(600, 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")



game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(snake.moving_speed)
    snake.move_snake()
    if snake.segments[0].distance(food)<15:
        food.reset()
        scoreboard.increase_score()
        snake.extend_snake()

    if snake.segments[0].xcor()<-290 or snake.segments[0].xcor()>290 or snake.segments[0].ycor()<-290 or snake.segments[0].ycor()>290:
        scoreboard.game_over()
        game_is_on=False

    # for i in range(1,len(snake.segments)-1):
    #     if snake.segments[0].distance(snake.segments[i]) < 20:
    #         scoreboard.game_over()
    #         game_is_on = False






screen.exitonclick()
