# turtle race 

from turtle import Turtle , Screen 

tim = Turtle()
screen = Screen()

screen.setup(width = 500 , height = 400)

user_bet = screen.textinput(title = "make your bet" , prompt = "which turtle will win the race: Enter a color : ")