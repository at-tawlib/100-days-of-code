from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """build a new score board with the attributes below"""
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """updates the scoreboard with the new score"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", font=FONT, align=ALIGNMENT)

    def reset(self):
        """if score greater than high_score, replace high_score"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """increases the score by 1, then updates it"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
