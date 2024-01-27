from turtle import Turtle



class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments=[]
        self.SEGMENTS_POSITION=[(0,0),(-20,0),(-40,0)]
        self.create_snake()
        self.moving_speed=0.2




    def create_snake(self):
        for position in self.SEGMENTS_POSITION:
            turtle = Turtle("square")
            turtle.fillcolor("white")
            turtle.pu()
            turtle.goto(position)
            self.segments.append(turtle)

    def move_snake(self):
        for i in range(len(self.segments)-1,0,-1):
            x_cor = self.segments[i-1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor,y_cor)

        self.segments[0].fd(20)


    def extend_snake(self):
        turtle = Turtle("square")
        turtle.fillcolor("white")
        turtle.pu()
        self.segments.append(turtle)
        self.moving_speed*=0.9

    def move_up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading()!=90:
            self.segments[0].setheading(270)

    def move_right(self):
        if self.segments[0].heading()!=180:
            self.segments[0].setheading(0)

    def move_left(self):
        if self.segments[0].heading()!=0:
            self.segments[0].setheading(180)


