from turtle import Turtle

EXTREMITY = 345
INITIAL_POINT = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def reset_the_ball(self):
        self.move_speed = 0.1
        self.goto(INITIAL_POINT)
        self.collision_bar()

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision_wall(self):
        self.y_move *= -1
        self.move_speed *= 0.7

    def collision_bar(self):
        self.x_move *= -1

    def goal_detection(self):
        if self.xcor() <= -EXTREMITY or self.xcor() >= EXTREMITY:
            return True
        return False


