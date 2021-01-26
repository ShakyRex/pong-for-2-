from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.l_score} Score: {self.r_score}', move=False, align=ALIGNMENT, font=FONT)

    def point_for_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def point_for_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()