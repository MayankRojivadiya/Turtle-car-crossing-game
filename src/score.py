from turtle import Turtle

FONT = ("Courier", 15, "bold")
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scr = 1
        self.color("white")
        self.penup()
        self.goto(-230,245)
        self.score_update()
        self.hideturtle()
        
    def score_update(self):
        self.clear()
        self.write(f"Level:{self.scr}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("white")
        self.write("Game Over", align=ALIGNMENT, font=("Courier", 24, "bold"))