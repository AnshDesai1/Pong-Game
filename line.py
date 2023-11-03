from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.pendown()
        self.color("White")
        self.width(5)
        self.setheading(270)
        while self.ycor() > -250:
            self.pendown()
            self.forward(25)
            self.penup()
            self.forward(25)

    def end_game(self):
        self.clear()