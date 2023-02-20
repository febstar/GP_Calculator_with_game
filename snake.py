from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.lists = []
        self.create_snake()
        self.head = self.lists[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_seg(position)

    def add_seg(self, position):
        new = Turtle()
        new.penup()
        new.color("white")
        new.shape("square")
        new.goto(position)
        self.lists.append(new)


    def extend(self):
        self.add_seg(self.lists[-1].position())


    def reset(self):
        for seg in self.lists:
            seg.goto(1000, 1000)
        self.lists.clear()
        self.create_snake()
        self.head = self.lists[0]

    def move(self):
        for seg_num in range(len(self.lists) - 1, 0, -1):
            new_x = self.lists[seg_num - 1].xcor()
            new_y = self.lists[seg_num - 1].ycor()
            self.lists[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)






    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
