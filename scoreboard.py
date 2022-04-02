from turtle import Turtle
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self, position ):
        super().__init__()
        self.score = 0
        self.shape("arrow")
        self.hideturtle()
        self.pencolor("white")
        self.up()
        self.goto(position)

    def draw_middle_line(self):
        self.setheading(270)
        while self.ycor() > -200:
            self.down()
            self.forward(10)
            self.up()
            self.forward(5)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", move=False, font=FONT)
