from turtle import Turtle



# food class inheriting from the turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        