#!/usr/bin/env python3
import turtle
import time
import geocoder
from pprint import pprint
from datetime import datetime
from PIL import Image

print("\n\n\n\nYou Are Here (f) Gazstao 2022-09-05 14h58")
agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(agora)

#
# localize me
#

g = geocoder.ip('me')
print("Sua localizacao atual aproximada é "+str(g.latlng))

#
# ajustando o mapa mundi
#

screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,190,90)
screen.bgpic("./map.gif")
screen.register_shape("./pin.gif")
you = turtle.Turtle()
you.penup()
you.shape("./pin.gif")

lat = g.latlng[0]
lon = g.latlng[1]
you.goto(lon,lat)

canvas = screen.getcanvas()
canvas.postscript(file="youarehere.eps", colormode="color")
img = Image.open("youarehere.eps")
img.save("youarehere.png")

time.sleep(30)
