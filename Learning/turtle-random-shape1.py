from turtle import *
import random

title('Gazstao Funny Shape')
bgcolor('black')
speed(0)
hideturtle()
colormode(255)
#pensize(1)
setposition([10,10])
for i in range (3500):
    action = random.randint(0,5)
    if (action<1):
        right(random.randint(3,10))
    elif (action<2):
        left(random.randint(3,10))
    elif (action<3):
        backward(random.randint(3,10))
    elif(action<4):
        forward(random.randint(3,10))
    else:
        color(random.randint(200, 255), 
        random.randint(100, 255), 
        random.randint(0, 55))
    right(45)
    forward(1)
done()