__author__ = 'student'
import turtle


def sneg(l):
    x = l / 3
    turtle.forward(x)
    turtle.left(60)
    turtle.forward(x)
    turtle.right(120)
    turtle.forward(x)
    turtle.left(60)
    turtle.forward(x)

sneg(400)
turtle.right(120)
sneg(400)
turtle.right(120)
sneg(400)


turtle.speed(1)