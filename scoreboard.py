from turtle import Turtle

FONT = ("Courier", 80, "normal")
END_GAME_FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.l_win = 0
        self.r_win = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def check_win(self):
        if self.r_score == 10:
            self.r_win = 1
            return True
        elif self.l_score == 10:
            self.l_win = 1
            return True

    def end_game(self):
        self.goto(0, 0)
        if self.r_win == 1:
            self.write("GAME OVER: RED PLAYER WINS!", align=ALIGNMENT, font=END_GAME_FONT)
        elif self.l_win == 1:
            self.write("GAME OVER: BLUE PLAYER WINS!", align=ALIGNMENT, font=END_GAME_FONT)



