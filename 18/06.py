# random movement of turtle

from turtle import Turtle, Screen
import random 

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed("fastest") 

colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "gray", "turquoise", "gold", "navy",
    "lime", "maroon", "coral", "indigo", "violet"
]

directions = [0 , 90 , 180 , 270]


for _ in range(300):
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()