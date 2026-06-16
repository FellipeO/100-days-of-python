from turtle import Turtle

WRITING_POS = (0, 270)
ALIGNMENT = "center"
FONT = ("courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

    def write_score(self):
        self.goto(WRITING_POS)
        self.clear()
        self.write(f"Score : {self.score}",align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)