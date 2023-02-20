from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.highscore = 0
        self.penup()
        self.goto(0, 250)
        with open("data.txt") as file:
            self.score = 0
            self.highscore = int(file.read())
            self.write(f"Score: {self.score} Highscore: {self.highscore}", move=False, align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align='center', font=('Spooky', 20, 'normal'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align='center', font=('Arial', 20, 'normal'))
