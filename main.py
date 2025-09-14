import time

from pingponggame import Paddle, Ball
from turtle import Screen
from scoreboard import Scorebaord

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600 )
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Scorebaord()
scoreboard.updatescore()
gameon = True
while gameon:
    time.sleep(0.1)
    screen.update()
    ball.move()
    #detect collition with wall
    if ball.ycor() >= 280 or ball.ycor() <= -300:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.x_bounce()

    if ball.xcor() >= 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() <= -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()