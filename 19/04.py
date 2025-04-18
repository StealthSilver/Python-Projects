# Turtle race game

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'green', 'yellow', 'blue', 'orange', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create and place turtles
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# Start race if user placed a bet
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # Check if any turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
            break  

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance) 

screen.exitonclick()
