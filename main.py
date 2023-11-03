from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

# Set up menu
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Generate sprites
r_paddle = Paddle((350, 0), "red")
l_paddle = Paddle((-350, 0), "blue")
line = Line()
ball = Ball()
scoreboard = Scoreboard()

# Allow playability
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect ball collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collisions with left and right wall
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Right player loses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Left player loses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # Declare Winner
    if scoreboard.check_win():
        game_is_on = False
        l_paddle.end_game()
        r_paddle.end_game()
        ball.end_game()
        line.end_game()
        scoreboard.end_game()

screen.exitonclick()
