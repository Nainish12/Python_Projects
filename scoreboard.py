from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        with open('data.txt', mode='r') as file:
            self.highscore = int(file.read())
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score = {self.score} High Score = {self.highscore}', move=False, align= ALIGNMENT, font=FONT )

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_score()

    # def game_over_dashboard(self):
    #     self.goto(0, 0)
    #     self.write(arg='Game Over', move=False, align= ALIGNMENT, font=FONT )
    def score_increase(self):
        self.score += 1
        self.update_score()
