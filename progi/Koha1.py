__author__ = 'student'
import turtle

def draw(l, n):
    if n == 0:
        turtle.forward (l)
        return

    x = l
    # for i in range (n):/
    #turtle.forward(x)
    draw(x /3 ,n-1)
    turtle.left(60)
    #turtle.forward(x)
    draw(x/3,n-1)
    turtle.right(120)
    #turtle.forward(x)
    draw(x/3,n-1)
    turtle.left(60)
    #turtle.forward(x)
    draw(x/3,n-1)

    #turtle.left(180)
    #turtle.penup()
    #turtle.forward(l)
    #turtle.pendown()
    #turtle.left(180)

draw(400,4)


turtle.speed(0)
