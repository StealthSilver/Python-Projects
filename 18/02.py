# types of imports 


# Basic import
import turtle 
tim = turtle.Turtle()


# for multiple imports
from turtle import Turtle 

tom = Turtle()
pop = Turtle()

# importing everything 
from turtle import *

# alias mdules 
import turtle as t

tommy = t.Turtle()

# installing modules
# pip install heroes

import heroes  # type: ignore
print(heroes.gen())
