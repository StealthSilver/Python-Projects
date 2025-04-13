from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")
timmy.color("black")

screen = Screen()


screen.setworldcoordinates(-500, -500, 500, 500)  


def polygon(sides):
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)


for sides in range(3, 31):
    polygon(sides)


screen.exitonclick()
