import time
from turtle import Screen
from wall import Wall
from player import Player
from ball import Ball
from scoreboard import ScoreBoard

import random
ekran=Screen()
ekran.setup(1000,600)
ekran.bgcolor("black")
ekran.tracer(0)
zid=Wall()
rezultat1=ScoreBoard(-40)
rezultat2=ScoreBoard(40)
left_paddle=Player((-450,0))
right_paddle=Player((450,0))
lopta=Ball()



ekran.listen()
ekran.onkey(fun=right_paddle.up_a,key="Up")
ekran.onkey(fun=right_paddle.down_a,key="Down")
ekran.onkey(fun=left_paddle.up_b,key="w")
ekran.onkey(fun=left_paddle.down_b,key="s")
game_is_on=True
broj=0.06

# x = random.choice([-10, 10])
# y = random.choice([-10, 10])
while game_is_on:

    time.sleep(broj)
    ekran.update()
    lopta.move()
    if lopta.ycor()>280 or lopta.ycor()<-280:
        lopta.bounce_y()
    if lopta.distance(right_paddle)<44 and lopta.xcor()>430 or lopta.distance(left_paddle)<44 and lopta.xcor()<-430:
        lopta.bounce_x()
        broj*=0.9
    if lopta.xcor()>490 or lopta.xcor()<-490:
        if lopta.xcor()>0:
            rezultat1.add_to_go()
            broj=0.06
            lopta.bounce_x()
            lopta.random_choose()

        else:
            rezultat2.add_to_go()
            broj=0.06
            lopta.bounce_x()
            lopta.random_choose()
        if rezultat2.gol==3:
            game_is_on=False
            rezultat1.game_over()
        if rezultat1.gol==3:
            game_is_on=False
            rezultat2.game_begin()
        lopta.goto(0,0)
        left_paddle.goto(-450,0)
        right_paddle.goto(450,0)


ekran.exitonclick()