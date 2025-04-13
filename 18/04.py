# creating different shapes in turtle

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")


def triangle():
    for _ in range(3):
        timmy.forward(100)
        timmy.right(120)

def square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def rectangle():
    for _ in range(2):
        timmy.forward(100)
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)

def pentagon():
    for _ in range(5):
        timmy.forward(100)
        timmy.right(72)

def polygon(sides):
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)

for _ in range(20):
    polygon(_)

screen = Screen()
screen.exitonclick()