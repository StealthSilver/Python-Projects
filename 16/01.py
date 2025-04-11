# Creating objects

from turtle import Turtle , Screen

# constructing the object and naming it timmy 
timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("DarkCyan")
timmy.forward(100)

# screen is an object
my_screen  = Screen()

# the canvas height is the attribute
print(my_screen.canvheight)

# the exitonclick is the method
my_screen.exitonclick()

