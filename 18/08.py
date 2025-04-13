# creating a spirograph 

from turtle import Turtle, Screen
import random 

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed("fastest") 

screen = Screen()
screen.setworldcoordinates(-1000, -1000, 1000, 1000)  
screen.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    # generating the tuple for the random color
    random_color = (r , g, b)
    return random_color



screen.exitonclick()