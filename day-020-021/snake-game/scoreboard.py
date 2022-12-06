from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        """build a new score board with the attributes below"""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """updates the scoreboard with the new score"""
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        """prints Game Over"""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increases the score by 1, then updates it"""
        self.score += 1
        self.clear()
        self.update_scoreboard()
