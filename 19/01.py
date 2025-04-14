# Event Listners

from turtle import Turtle , Screen 

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()

# higher order function -> function as an input
screen.onkey(key = "space" , fun = move_forwards)

screen.exitonclick()