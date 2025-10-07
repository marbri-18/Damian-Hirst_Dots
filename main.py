import turtle
from turtle import Screen
import random
#import colorgram

turtle.colormode(255)
colour_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.color("cadet blue")

tim.penup()
tim.goto(-300, -300)

for _ in range(5):
    for _ in range(10):
        dot_colour = random.choice(colour_list)
        tim.dot(20, dot_colour)
        tim.forward(50)

    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    for _ in range(10):
        dot_colour = random.choice(colour_list)

        tim.dot(20, dot_colour)
        tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)

screen = Screen()
screen.exitonclick()