#MINI-PROJECT TURTLE GRAPHICS INTIATION
import turtle
from random import randint
turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(1)
for i in range(1,364):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    turtle.colormode(255)
    turtle.pencolor(r,g,b)
    turtle.forward(50 + i)
    turtle.right(91)
    i+=2
turtle.done()
#PROJECTED SUCCESSFULLY COMPLETED
#NAME : KANURI TEJA SAI VAMSI
