from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()
