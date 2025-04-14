# turtle race 

from turtle import Turtle , Screen 


screen = Screen()

screen.setup(width = 500 , height = 400)

user_bet = screen.textinput(title = "make your bet" , prompt = "which turtle will win the race: Enter a color : ")


tim = Turtle()
tim.goto(x = -250 , y = -100)

screen.exitonclick()