
import turtle
import keyboard
import time

print ("Gazstao The System v1.0 2022.08.31 21h49\n")

run = True

turtle.setup(1400,900)
turtle.speed(0)
turtle.bgcolor('black')
turtle.color('blue')

while run:
    if keyboard.is_pressed('w'):
        turtle.forward(1)
    if keyboard.is_pressed('s'):
        turtle.backward(1)
    if keyboard.is_pressed('a'):
        turtle.left(15)
        time.sleep(.1)
    if keyboard.is_pressed('d'):
        turtle.right(15)
        time.sleep(.1)
    if keyboard.is_pressed('*'):
        run = False
    if keyboard.is_pressed(' '):
        if turtle.isdown():
            turtle.color('red')
            turtle.penup()
            time.sleep(.5)
        else:
            turtle.color('blue')
            turtle.pendown()
            time.sleep(.5)
    if keyboard.is_pressed('C'):
        turtle.clear()
    if keyboard.is_pressed('e'):
        turtle.color('black')