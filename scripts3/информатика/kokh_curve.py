import turtle
from random import random, randrange
def koch_curve(turtle, steps, length):
    if steps == 0:
        turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, steps - 1, length / 3)
            turtle.left(angle)
turtle.reset()
turtle.penup()
turtle.setpos(-150,150)
turtle.pendown()
#print(turtle.pos())
#print(turtle.screensize())
#print(turtle.window_height())
#print(turtle.window_width())
turtle.speed("fastest")
turtle.ht()
#turtle.begin_poly()
for _ in range(3):
    koch_curve(turtle.getturtle(),3 ,300)
    turtle.right(120)
#turtle.end_poly()
turtle.done()
