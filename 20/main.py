from turtle import Screen, Turtle 
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



segments = []

# initializing the snake
for position in starting_positions:
    
game_is_on = True 

# motion of the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
   
    

screen.exitonclick()
