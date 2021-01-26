from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from score_board import Score_board


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Score_board()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    # this slows down the loop and so the ball
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 330 and ball.distance(r_paddle) <= 35 or ball.xcor() < -330 and ball.distance(l_paddle) <= 35:
        ball.bounce_on_paddle()

    if ball.xcor() < -345:
        score_board.point_for_r()
        ball.reset_position()

    if ball.xcor() > 345:
        score_board.point_for_l()
        ball.reset_position()


screen.exitonclick()
