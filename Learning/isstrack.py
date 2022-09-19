#!/usr/bin/env python3
import json
import turtle
import urllib.request
import time
from PIL import Image
import geocoder
from pprint import pprint
from datetime import datetime
import keyboard

#
# inicializa o programa
#

url_astros = "http://api.open-notify.org/astros.json"
url_iss = "http://api.open-notify.org/iss-now.json"
d = 1 #diametro do ponto

print("\n\n\n\nISS Tracking (f) Gazstao 2022-02-09 20h39 - Searching at "+url_astros+" em ",end="")
agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
horaExecucao = datetime.now().strftime("%Y.%m.%d-%H.%M")
print(agora)

#
# obtem os dados em formato json
#

response = urllib.request.urlopen(url_astros)
result = json.loads(response.read())
pprint(result)

#
# grava arquivo iss.txt
#

file = open("iss.txt","w")
file.write(
    "ISS Tracking (f) Gazstao V0.220209.2039 - Searching at "+url_astros+" e "+url_iss+"\n"+
    "Existem atualmente "+str(result["number"])+
    " astronautas no espaco "+agora+" \n\n")

people = result["people"]
for p in people:
    file.write(p['name']+" - on board of "+ p['craft']+"\n")

#
# localize me
#

g = geocoder.ip('me')
file.write("\nSua localizacao atual aproximada eh "+str(g.latlng)+"\n")
print("Sua localizacao atual aproximada é "+str(g.latlng))

#
# ajustando o mapa mundi
#

screen = turtle.Screen()
screen.setup(1280,720)
screen.setworldcoordinates(-180,-90,190,90)
screen.bgpic("map.gif")
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(45)
iss.penup()

#
# obtendo posicao da ISS
#

lon = -180.0
rodando = True

while rodando:
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    response = urllib.request.urlopen(url_iss)
    result = json.loads(response.read())
    lastLon = lon

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    #print("Lat ant: {}".format(antLon))
    lat = float(lat)
    lon = float(lon)

    print("ISS Latitude: "+str(lat)+ " Longitude: "+str(lon)+" em "+agora+" - last longitude: "+str(lastLon))
    file.write("\nISS Latitude: "+str(lat)+ " Longitude: "+str(lon)+" em "+agora)

    iss.goto(lon,lat)
    cwd = iss.position() 
    iss.color = "Red"
    iss.pendown()
    #iss.forward(d)
    #iss.left(90)
    #iss.forward(d)
    #iss.left(90)
    #iss.forward(d)
    #iss.left(90)
    #iss.forward(d)
    #iss.left(90)
    if (lon < lastLon):
        iss.penup()
    iss.goto(cwd) # POP retrieve back to enter state
    canvas = screen.getcanvas()
    canvas.postscript(file="iss.eps", colormode="color")
    img = Image.open("iss.eps")
    img.save("iss-{}.png".format(horaExecucao))
    for i in range(10):
        if keyboard.is_pressed("q"):
            resp = input("Encerra (s/n)?")
            if (resp == "s"):
                rodando = False
                file.close()
                print("encerrando...")
                break
        time.sleep(2)
