from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, starting_x_position, starting_y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(starting_x_position, starting_y_position)

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)

