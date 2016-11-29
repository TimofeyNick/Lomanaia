__author__ = 'student'
import turtle as tr

def draw(l, n):
    if n == 0:
        tr.forward (l)
        return

    x = l / 4
    #tr.forward(x)
    draw(x, n-1)
    tr.left(90)
    #tr.forward(x)
    draw(x, n-1)
    tr.right(90)
    #tr.forward(x)
    draw(x, n-1)
    tr.right(90)
    #tr.forward(2*x)
    draw((x), n-1)
    draw((x), n-1)
    tr.left(90)
    #tr.forward(x)
    draw(x, n-1)
    tr.left(90)
    #tr.forward(x)
    draw(x, n-1)
    tr.right(90)
    #tr.forward(x)
    draw(x, n-1)


draw(400,3)
tr.speed(2)