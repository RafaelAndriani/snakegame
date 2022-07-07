from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.setposition(0, 250)
        self.color("white")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.setposition(0, 150)
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()