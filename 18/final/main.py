# creating the Hirst Painting

import turtle as turtle_module 
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")

# the color list from the colorgram and demo.jpeg
color_list = [(155, 80, 50), (21, 29, 67), (194, 153, 133), (36, 104, 164), (122, 166, 193), (246, 219, 70), (158, 66, 100), (24, 49, 129), (171, 154, 160), (65, 24, 40), (68, 30, 16), (118, 189, 152), (120, 30, 53), (224, 84, 50), (20, 88, 38), (197, 81, 117), (127, 32, 15), (57, 126, 50), (55, 125, 210), (253, 216, 0), (9, 86, 107), (16, 64, 36), (177, 167, 52), (211, 180, 188), (71, 175, 111), (226, 177, 167), (182, 189, 209), (85, 145, 160), (165, 209, 183), (158, 205, 216), (69, 71, 24)]


tim.heading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1 , number_of_dots):
    tim.dot(20 , random.choice(color_list))
    tim.forward(50)


    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.heading(0)
    




screen = turtle_module.Screen()
screen.exitonclick()