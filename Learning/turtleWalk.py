import turtle

x=140*9
y=140*6
escala = 140

def vaiPra(xis,ypslon):
    turtle.penup()
    turtle.goto(-x/2+xis,y/2-ypslon)
    turtle.pendown()

def goTo(xis, yps):
    turtle.goto(-x/2+xis,y/2-yps)


def teia_de_aranha(ate = 500, passo = 0.75, cor='green'):
    turtle.color(cor)
    for i in range (ate):
        turtle.right(45)
        turtle.forward(i*passo)

def espiral(ate = 500, passo = 20, abertura = 10, cor = 'white'):
    turtle.color(cor)
    for i in range(ate):
        turtle.right(abertura)
        turtle.forward(i/passo)

def espiralCanhota(ate = 500, passo = 20, abertura = 10, cor = 'white'):
    turtle.color(cor)
    for i in range(ate):
        turtle.left(abertura)
        turtle.forward(i/passo)

turtle.speed(0)
turtle.bgcolor('black')
turtle.color('blue')
turtle.setup(x,y)
turtle.hideturtle()

vaiPra(0,0)

turtle.clear()

turtle.color('blue')
for i in range(int(y/escala)+1):
    vaiPra(0,i*escala)
    goTo(x,i*escala)

for i in range(int(x/escala)+1):
    vaiPra(i*escala,0)
    goTo(i*escala,y)

escala = 14

for i in range(int(y/escala)+1):
    vaiPra(0,i*escala)
    goTo(x,i*escala)

for i in range(int(x/escala)+1):
    vaiPra(i*escala,0)
    goTo(i*escala,y)

vaiPra(int(x/2),int(y/2))
espiral(ate=1400,cor='green')

vaiPra(int(x/2),int(y/2))
espiralCanhota(ate=1400,cor='green')

turtle.done()