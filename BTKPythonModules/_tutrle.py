"""import turtle
isaretci=turtle.Turtle()
isaretci.screen.setup(width=1000,height=550)
isaretci.speed(0)
isaretci.screen.bgcolor("red")
isaretci.hideturtle()
def konumla_boya(renk,yatay,dikey):
    isaretci.penup()
    isaretci.goto(yatay,dikey)
    isaretci.pendown()
    isaretci.color(renk)
    isaretci.begin_fill()

def star(boy):
    konumla_boya("white",77,64)
    for i in range(5):
        if i ==0:
            derece=125
        else:
            derece=144
        isaretci.right(derece)
        isaretci.forward(boy)
    isaretci.end_fill()

def daire(cap):
    isaretci.circle(cap)
    isaretci.end_fill()

konumla_boya("white", -175, -130)
daire(150)
konumla_boya("red", -140, -99)
daire(120)


star(130)



isaretci.screen.mainloop()
"""
import turtle
from math import cos,radians
isaretci = turtle.Turtle()
isaretci.screen.setup(width=1300, height=700)
isaretci.speed(0)
isaretci.hideturtle()

def konumla_boya(renk, yatay, dikey):
    isaretci.penup()
    isaretci.goto(yatay, dikey)
    isaretci.pendown()
    isaretci.color(renk)
    isaretci.begin_fill()

def star(boy, x, y):
    konumla_boya("white", x, y)
    isaretci.left(36)
    isaretci.forward(boy / 2)

    for i in range(6):
        if i == 0:
            derece = 160
        else:
            derece= 144
        if i==5:
            derece=109
            isaretci.left(derece)
            isaretci.penup()
            isaretci.end_fill()
            return
        isaretci.left(derece)
        isaretci.forward(boy)
    isaretci.end_fill()

def daire(cap):
    isaretci.circle(cap)
    isaretci.end_fill()

def dikdortgen(g):
    for t in range(2):
        isaretci.forward(g * 1.5)
        isaretci.left(90)
        isaretci.forward(g)
        isaretci.left(90)

def bayrakciz(g,xkonum,ykonum):
    konumla_boya("red", xkonum,ykonum)
    dikdortgen(g)
    isaretci.end_fill()
    a =g/2
    b= g /4
    c=g/16
    d=g/5
    e=g/3
    f=g/8
    l=g*1.5
    starx=a+c+e-d+f
    stary=g/2
    konumla_boya("white", (g / 2)+xkonum, (g / 4)+ykonum)
    daire(g / 4)
    konumla_boya("red", (g / 2) + (g / 16)+xkonum, (g / 2) - (g /5)+ykonum)
    daire(g / 5)
    star_boy=(f+(cos(radians(36))*f))/cos(radians(18))
    star(star_boy,starx+xkonum,stary+ykonum)
    isaretci.right(161)

ilksatir=250
ilksutun=-650
for satir in range(6):
    for sutun in range(9):
        bayrakciz(100, ilksutun, ilksatir)
        ilksutun += 155
    ilksatir-=105
    ilksutun=-650



isaretci.screen.mainloop()

