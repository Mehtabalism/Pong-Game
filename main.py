from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_1 = Paddle(-350, 0)
player_2 = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=player_1.up)
screen.onkeypress(key="s", fun=player_1.down)
screen.onkeypress(key="Up", fun=player_2.up)
screen.onkeypress(key="Down", fun=player_2.down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(player_1) < 50 and ball.xcor() < -320 or ball.distance(player_2) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # Detect score
    if ball.xcor() > 380:
        scoreboard.player_1_scores()
        scoreboard.update()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.player_2_scores()
        scoreboard.update()
        ball.reset_position()

screen.exitonclick()

