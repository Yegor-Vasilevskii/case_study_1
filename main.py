# Case_1
#developers: Pokareva Christina (75%)
#            Pestretsova Margarita
#            Vasilevsky Egor
import turtle

def square (x, y, size, color, angele)
    #TODO: (Yegor-Vasilevskii) поставить задачу всем, ну и забабахать кукую-то деталь
    from turtle import *
color('red', 'yellow','blue','black','brown')






def traingle (x1, y1, x2, y2, x3, y3, f_color='white')
    #TODO: (MargaritaPestretsova)
  
import turtle
import math


def traingle(x1, y1, x2, y2, x3, y3, f_color='white'):

    """
    function  which describes the traingle
    :param x1: position of the first point horizontal 
    :param y1: position of the first point vertical
    :param x2: position of the second point horizontal
    :param y2: position of the second point vertical
    :param x3: position of the third point horizontal
    :param y3: position of the third point vertical

    """
    turtle.speed(7)
    turtle.color(f_color)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(x1, y1)

    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()
    turtle.penup()


traingle(100, -20, 40, -30, 70, -50, f_color='red')

turtle.done()



#TODO (ChristinaPokareva)
turtle.hideturtle()
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.circle()
turtle.end.fill()

turtle.hideturtle()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.forward (100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(100)
turtle.forward(100)
turtle.end_fill()

def all figures (x, y, size, color, angele)
#TODO (StepanDt)


pass
