from turtle import Turtle
from random import randint



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.shapesize(0.5,0.5)
        self.pu()
        self.create_food()

    def create_food(self):
        PODITION_X = randint(-270, 270)
        PODITION_Y = randint(-270, 270)
        self.goto(PODITION_X,PODITION_Y)

    def reset(self):
        PODITION_X = randint(-270, 270)
        PODITION_Y = randint(-270, 270)
        self.goto(PODITION_X, PODITION_Y)


