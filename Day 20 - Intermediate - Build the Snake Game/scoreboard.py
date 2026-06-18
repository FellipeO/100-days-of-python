from turtle import Turtle

WRITING_POS = (0, 270)
ALIGNMENT = "center"
FONT = ("courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.hideturtle()

    def write_score(self):
        self.goto(WRITING_POS)
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.high_score}",align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def reset(self):
        if self.score >self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()
