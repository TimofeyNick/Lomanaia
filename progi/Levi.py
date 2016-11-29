__author__ = 'student'
import turtle as tr

def draw(l, n):
    if n == 0:
        tr.forward (l)
        return

    x = l / ((2)**0.5)
    tr.left(45)
    #tr.right((n-1)*45)
    #tr.forward(x)
    draw(l / 2, n-1)
    tr.right(90)
    #tr.forward(x)
    draw(l / 2, n-1)
    tr.left(45)
    # Must return in the same first direction

draw(1000, 7)
tr.speed(0)