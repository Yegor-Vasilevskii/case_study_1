# Case_1
#developers: Pokareva Christina (75%)
#            Pestretsova Margarita
#            Vasilevsky Egor (50%)
import turtle

    #TODO: (Yegor-Vasilevskii) 2 фигуры
 #fig 1
import turtle
win = turtle.Screen()
turtle.shape('turtle')
turtle.speed(0)

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.write('Фигура 1')

turtle.penup()
turtle.goto(-330,180)
turtle.pendown()
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.penup()
turtle.goto(-290,140)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.forward(140)
turtle.right(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(140)
turtle.right(90)
turtle.forward(140)
turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,180)
turtle.pendown()
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.penup()
turtle.goto(50,40)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

turtle.penup()
turtle.goto(140,180)
turtle.pendown()
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.forward(220)
turtle.right(90)
turtle.penup()
turtle.goto(215,180)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.forward(70)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(70)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,210)
turtle.pendown()
turtle.write('К 140-летию К. Малевича посвящается')


#Fig 2
turtle.penup()
turtle.goto(-200,-120)
turtle.pendown()
turtle.write('Фигура 2')

turtle.penup()
turtle.goto(-20,-110)
turtle.pendown()
turtle.fillcolor('black')
turtle.begin_fill()
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(170)
turtle.right(90)
turtle.forward(80)
turtle.right(90)
turtle.forward(170)
turtle.end_fill()

turtle.penup()
turtle.goto(45,-145)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(23)
turtle.end_fill()
turtle.penup()
turtle.goto(45,-198)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(23)
turtle.end_fill()
turtle.penup()
turtle.goto(45,-250)
turtle.pendown()
turtle.fillcolor('green')
turtle.begin_fill()
turtle.circle(23)
turtle.end_fill()

win.exitonclick()

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
