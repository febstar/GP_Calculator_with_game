from turtle import Turtle
import secrets


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid= 0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = secrets.SystemRandom().randint(-250, 250)
        random_y = secrets.SystemRandom().randint(-250, 250)
        self.goto(random_x, random_y)

