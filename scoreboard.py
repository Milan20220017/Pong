from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self,udaljenost):
        super().__init__()
        self.gol=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(udaljenost,260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(self.gol,move=False,align="Center",font=("Verdana",29,"bold"))
    def add_to_go(self):
        self.gol+=1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("Player 2 won", move=False, align="Center", font=("Courier", 40, "normal"))
    def game_begin(self):
        self.goto(0, 0)
        self.write("Player 1 won", move=False, align="Center", font=("Arial", 40, "normal"))


