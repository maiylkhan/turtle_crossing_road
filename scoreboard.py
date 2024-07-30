from turtle import Turtle
FONT = ("Courier", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color = "black"
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-220, 250)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=FONT)

    def update_score(self):
        self.level += 1
        self.display_score()





