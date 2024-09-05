from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.seg_head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_seg(pos)
    def add_seg(self,position):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.seg_head = self.segments[0]

    def extend_snake(self):
        self.add_seg(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_asx = self.segments[seg - 1].xcor()
            y_asx = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_asx, y_asx)
        self.segments[0].forward(MOVE_DIS)

    def up(self):
        if self.seg_head.heading() != DOWN:
            self.seg_head.setheading(UP)

    def down(self):
        if self.seg_head.heading() != UP:
            self.seg_head.setheading(DOWN)

    def left(self):
        if self.seg_head.heading() != RIGHT:
            self.seg_head.setheading(LEFT)

    def right(self):
        if self.seg_head.heading() != LEFT:
            self.seg_head.setheading(RIGHT)
