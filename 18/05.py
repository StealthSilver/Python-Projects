# get a all figure shape

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")
timmy.speed("fastest") 

screen = Screen()


screen.setworldcoordinates(-1000, -1000, 1000, 1000)  



def polygon(sides):
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)


for sides in range(3, 31):
    polygon(sides)


screen.exitonclick()
