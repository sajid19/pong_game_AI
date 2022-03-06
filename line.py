from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=50, stretch_len=0.2)

