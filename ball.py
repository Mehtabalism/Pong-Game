from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.04
        # Code using headings
        # self.setheading(45)

        # Code using steps
        self.x_step = 10
        self.y_step = 10

    def move(self):
        # Code using headings
        # self.forward(10)

        # Code using steps
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Code using headings
        # if 0 < self.heading() < 90:
        #     self.setheading(self.heading() + 270)
        # elif 90 < self.heading() < 180:
        #     self.setheading(self.heading() + 90)
        # elif 180 < self.heading() < 270:
        #     self.setheading(self.heading() - 90)
        # elif 270 < self.heading() < 360:
        #     self.setheading(self.heading() - 270)
        # elif self.heading() == 90:
        #     self.setheading(270)
        # elif self.heading() == 270:
        #     self.setheading(90)

        # Code using steps
        self.y_step *= -1

    def bounce_x(self):
        self.move_speed *= 0.9
        # Code using headings
        # if 0 < self.heading() < 90:
        #     self.setheading(self.heading() + 90)
        # elif 90 < self.heading() < 180:
        #     self.setheading(self.heading() - 90)
        # elif 180 < self.heading() < 270:
        #     self.setheading(self.heading() + 90)
        # elif 270 < self.heading() < 360:
        #     self.setheading(self.heading() - 90)
        # elif self.heading() == 0:
        #     self.setheading(180)
        # elif self.heading() == 180:
        #     self.setheading(0)

        # Code using steps
        self.x_step *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.04
        self.x_step *= -1
