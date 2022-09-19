from turtle import *
import random

x = 1400
y = 900

print("\n\nStarting...\n\n")
title('Gazstao Funny Shape')
setup(x,y)
bgcolor('black')
colormode(255)
speed(0)
goto(0,0)
hideturtle()

fim = 200 # repeticoes, quanto mais, mais complexo maior e mais demorado

def espiral_quadros(ate = 1000, cor='yellow'):
    color(cor)
    for i in range (ate):
        right(50)
        forward(i)
    goto(0,0)

def teia_de_aranha(ate = 1000, passo = 0.75, cor='green'):
    color(cor)
    for i in range (ate):
        title('Gazstao Funny Shape - Teia de Aranha - {}'.format(i))
        right(60)
        forward(i*passo)

def espiral(ate = 1000, passo = 20, abertura = 10, cor = 'green'):
    color(cor)
    for i in range(ate):
        title('Gazstao Funny Shape - Espiral - {} de {}'.format(i, ate))
        right(abertura)
        forward(i/passo)

def espiral_canhota(ate = 1000, passo = 20, abertura = 10, cor='blue'):
    color(cor)
    for i in range(ate):
        title('Gazstao Funny Shape - Espiral Canhota - {} de {}'.format(i, ate))
        left(abertura)
        forward(i/passo)

def vaiPra(x, y):
    penup()
    goto(x,y)
    pendown()

def goRandom():
    up()
    goto (random.randint(1,x)-x/2,random.randint(1,y)-y/2)
    down()

pensize(2)
bgcolor('green')
for i in range(2):
    goRandom()
    espiral(cor='black', ate = random.randint(1,1000), passo=random.randint(1,25))
    goRandom()
    espiral_canhota(cor='black', ate = random.randint(1,1000), passo=random.randint(1,25))
bgcolor('gray')
clear()
vaiPra(0,0)
teia_de_aranha(passo=2.5, ate=fim)
vaiPra(0,0)
teia_de_aranha(passo=2.5, ate=fim, cor='yellow')
vaiPra(0,0)
pensize(15)
teia_de_aranha(passo=2.5, ate=fim, cor='black')
clear()
bgcolor('black')
vaiPra(0,0)
pensize(1)
espiral_canhota(cor='green', passo=10)
vaiPra(0,0)
espiral(color='red')
vaiPra(-300,0)
espiral_canhota(cor = 'blue', abertura=20, ate=300, passo=20)
vaiPra(-300,300)
espiral_canhota(cor = 'blue', abertura=15, ate=300, passo=20)
vaiPra(0,0)
espiral_canhota(cor = 'white', abertura=5, ate=300, passo = 100)
vaiPra(0,300)
espiral_canhota(cor = 'white', abertura=10, ate=300, passo = 100)
vaiPra(300,000)
espiral_canhota(cor = 'green', abertura=5, ate=300, passo = 20)
vaiPra(300,300)
espiral_canhota(cor = 'green', abertura=10, ate=300, passo = 20)
