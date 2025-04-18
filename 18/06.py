# random movement of turtle

from turtle import Turtle, Screen
import random 

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed("fastest") 

screen = Screen()
screen.setworldcoordinates(-1000, -1000, 1000, 1000)  


colors = [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "gray", "turquoise", "gold", "navy",
    "lime", "maroon", "coral", "indigo", "violet"
]

directions = [0 , 90 , 180 , 270]
timmy.pensize(10)

for _ in range(1000):
    timmy.color(random.choice(colors))
    timmy.forward(80)
    timmy.setheading(random.choice(directions))



screen.exitonclick()