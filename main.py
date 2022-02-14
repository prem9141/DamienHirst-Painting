from turtle import Turtle, Screen
import random
import colorgram


screen = Screen()
screen.colormode(255)
screen.title('DamienHirst Painting')

colors = colorgram.extract('image.jpg', 25)

turtle = Turtle()
turtle.shape()
turtle.color("green")
turtle.speed("fastest")
turtle.penup()
turtle.setpos(-150, -200)
turtle.pendown()
painting_space_hor = 30
painting_space_ver = 30

for pos in range(1, 101):
    color = random.choice(colors)
    color = (color.rgb.r, color.rgb.g, color.rgb.b)
    turtle.dot(15, color)
    turtle.hideturtle()
    turtle.penup()
    turtle.forward(painting_space_hor)
    turtle.pendown()

    if pos % 10 == 0:
        x, y = turtle.pos()
        turtle.penup()
        turtle.setx(x - 10*painting_space_hor)
        turtle.sety(y+painting_space_hor)
        turtle.pendown()

screen.exitonclick()
