from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(cor)
        self.setheading(90)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        newx =  self.xcor() + self.xmove
        newy =  self.ycor() + self.ymove
        self.goto(newx, newy)

    def y_bounce(self):
        self.ymove *= -1
        self.move_speed *= 0.9

    def x_bounce(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def bounce(self):
        self.x_bounce()
        self.y_bounce()

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_bounce()