# PART 1
# create two bart that block the ball
# from a class called bar class from the bar file
# the bark can be moved from up to down only
from turtle import Screen
import time
from ball import Ball
from receiver_bar import ReceiverBar
from scoreboard import Scoreboard


EXTREMITY_GOAL = 345
EXTREMITY_TOP_BOTTOM = 180
EXTREMITY_LEFT_RIGHT = 325
SCOREBOARD_POSITION = [(0, 200), (-30, 150), (30, 150)]

LEFT_EXTREMITY = (-345, 0)
RIGHT_EXTREMITY = (335, 0)
screen = Screen()
screen.bgcolor("black")
screen.title("My Pong Game")
screen.setup(width=700, height=400)
play_is_on = True
screen.tracer(0)
ball = Ball()
receiver_bar1 = ReceiverBar(LEFT_EXTREMITY)
receiver_bar2 = ReceiverBar(RIGHT_EXTREMITY)
middle_line = Scoreboard(SCOREBOARD_POSITION[0])
middle_line.draw_middle_line()
score_player1 = Scoreboard(SCOREBOARD_POSITION[1])
score_player2 = Scoreboard(SCOREBOARD_POSITION[2])

screen.listen()
screen.onkey(key="Up", fun=receiver_bar1.move_up)
screen.onkey(key="Down", fun=receiver_bar1.move_down)
screen.onkey(key="Left", fun=receiver_bar2.move_up)
screen.onkey(key="Right", fun=receiver_bar2.move_down)

while play_is_on:
    ball.move_ball()
    screen.update()
    score_player1.update_score()
    score_player2.update_score()

    if ball.ycor() <= -EXTREMITY_TOP_BOTTOM or ball.ycor() >= EXTREMITY_TOP_BOTTOM:
        ball.collision_wall()
    if (ball.distance(receiver_bar1) < 45 and ball.xcor() <= -EXTREMITY_LEFT_RIGHT) or (ball.xcor() >= EXTREMITY_LEFT_RIGHT and ball.distance(receiver_bar2) < 45):
        ball.collision_bar()

    if ball.goal_detection():
        if ball.xcor() <= -EXTREMITY_GOAL:
            score_player2.increase_score()
        elif ball.xcor() >= EXTREMITY_GOAL:
            score_player1.increase_score()
        ball.reset_the_ball()
    print(ball.xcor())

    if score_player1.score - score_player2.score == 3 or score_player1.score - score_player2.score == -3:
        play_is_on = False
    time.sleep(ball.move_speed)

# PART 2
# create a Ball in square format
# create a method that is used to move the ball when it touches the two bars and the up and down wall
# PART 3
# Screen design
# create a scoreboard class with some method
# That will increase the score when one team scores


screen.exitonclick()
