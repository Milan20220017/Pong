from turtle import Turtle
class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.goto(position)


    def up_a(self):
        if self.ycor() < 210:
            y=self.ycor()+80
            self.goto(self.xcor(),y)
    def down_a(self):
        if self.ycor() > -210:
            y = self.ycor() - 80
            self.goto(self.xcor(),y)
    def up_b(self):
        if self.ycor() < 210:
            y = self.ycor() + 80
            self.goto(self.xcor(),y)
    def down_b(self):
        if self.ycor() > -210:
            y = self.ycor() - 80
            self.goto(self.xcor(),y)



