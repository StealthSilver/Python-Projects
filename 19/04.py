# turtle race 

from turtle import Turtle , Screen 


screen = Screen()

screen.setup(width = 500 , height = 400)

user_bet = screen.textinput(title = "make your bet" , prompt = "which turtle will win the race: Enter a color : ")


tim = Turtle(shape = "turtle")
tim.penup()
tim.goto(x = -230 , y = -100)

screen.exitonclick()