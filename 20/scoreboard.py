from turtle import Turtle

class Scoreboard(Turtle):   

    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score: {self.score}" , aligh = "center" , font = ("Arial" , 24 , "normal"))