from turtle import Turtle
class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -270)
        self.pendown()
        self.pensize(5)
        self.setheading(90)
        for _ in range(23):
            self.forward(14)
            self.penup()
            self.forward(10)
            self.pendown()

