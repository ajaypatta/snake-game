from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.pu()
        self.hideturtle()
        self.score_level()

    def score_level(self):
        self.goto(-240,270)
        # with open("highest_score.txt") as file:
        #     self.highest_score = file.read()
        self.write(f"score: {self.score} ",align='center', font=('Arial', 10, 'normal'))

    def increase_score(self):
        self.score+=1
        with open("highest_score.txt", "w") as file:
            file.write(f"{self.score}")
        # if self.score > int(self.highest_score) :
        #     with open("highest_score.txt", "w") as file:
        #         file.write(f"{self.highest_score}")
        self.clear()
        self.score_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"game over! .", align='center', font=('Arial', 20, 'normal'))



