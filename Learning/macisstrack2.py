#!/usr/bin/env python3

# Referencia calculo de distancia: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
# Referencia exemplo base: 

import json
from os import times
from sqlite3 import Timestamp
import turtle
import urllib.request
import time
from PIL import Image
import geocoder
from pprint import pprint
from datetime import datetime
import keyboard
from math import *

#
# inicializa o programa
#

url_astros = "http://api.open-notify.org/astros.json"
url_iss = "http://api.open-notify.org/iss-now.json"

# HELLO 

print("\n\n****************************************\nISS Tracking (f) Gazstao 2022")
print("\n****************************************\n\n")

timeStamp = datetime.now()
agora = timeStamp.strftime("%d/%m/%Y %H:%M:%S")
horaExecucao = datetime.now().strftime("%Y.%m.%d-%H.%M")

print("Searching at "+url_astros+" em "+agora,end="")

#
# obtem os dados em formato json
#

response = urllib.request.urlopen(url_astros)
result = json.loads(response.read())
pprint(result)

#
# grava arquivo iss.txt
#

file = open("./Data/iss-{}.txt".format(horaExecucao),"w")
issdata = open("./Data/iss-{}.csv".format(horaExecucao),"w")

file.write(
    "ISS Tracking (f) Gazstao V1.220905.1631 - Searching at "+url_astros+" e "+url_iss+"\n"+
    "Existem atualmente "+str(result["number"])+
    " astronautas no espaco "+agora+" \n\n")
issdata.write("latitude, longitude, hora, velocidade\n")

# Mostra a lista de (astro/cosmo/taiko)nautas 
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
screen.title("Gazstao - ISS Tracking")
screen.setup(1420,720)
screen.setworldcoordinates(-180,-90,190,90)
screen.bgpic("./map2.gif")
screen.register_shape("./iss-icon.gif")
iss = turtle.Turtle()
iss.shape("./iss-icon.gif")
iss.setheading(45)
iss.penup()

lon = -180.0
lat = -90.0
rodando = True

file.close()
issdata.close()


while rodando:
    file = open("./Data/iss-{}.txt".format(horaExecucao),"a")
    issdata = open("./Data/iss-{}.csv".format(horaExecucao),"a")
    newTime = datetime.now()
    agora = time.strftime("%d/%m/%Y %H:%M:%S")
    
    try:
        response = urllib.request.urlopen(url_iss)
        result = json.loads(response.read())
        lastLon = lon
        lastLat = lat
    except:
        print("nao foi possivel acessar a API web")

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']
    screen.title("Gazstao ISS Tracking   Latitude:{}  Longitude:{} em {}".format(lat, lon, agora))

    #print("Lat ant: {}".format(antLon))
    lat = float(lat)
    lon = float(lon)

    if (lon < lastLon):
        iss.penup()
    
    iss.goto(lon,lat)
    #cwd = iss.position() 
    iss.color = "Red"
    iss.pendown()
    #iss.goto(cwd) # POP retrieve back to enter state
    canvas = screen.getcanvas()
    canvas.postscript(file="./iss.eps", colormode="color")
    img = Image.open("./iss.eps")
    img.save("./Data/iss-track-{}.png".format(horaExecucao))

    # calcula a distancia percorrida pelo tempo, e calcula a velocidade aproximada

    if (lastLon != -180.0 and lastLat != -90.0):
        lat1 = lastLat
        lat2 = lat
        lon1 = lastLon
        lon2 = lon
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distancia = 6371 * c

        deltaTime = (newTime - timeStamp).total_seconds()
        timeStamp = newTime
        velocidade = distancia*3600/deltaTime

        #print("Distancia: {}km   Tempo: {}s    Velocidade aproximada: {} km/h".format(distancia, deltaTime, int(velocidade)))
        string = "ISS Latitude: "+str(lat)+ " Longitude: "+str(lon)+"  Distancia percorrida: {}km   Tempo: {}s    Velocidade aproximada: {} km/h".format(distancia, deltaTime, int(velocidade))+" em "+agora
        print(string)
        file.write("\n"+string)
        issdata.write("{}, {}, {}, {}\n".format(lat, lon, newTime, velocidade))

    file.close()
    issdata.close()

    # encerra?

    for i in range(20):
        if keyboard.is_pressed("q"):
            resp = input("Encerra (s/n)?")
            if (resp == "s"):
                rodando = False
                print("encerrando...")
                break
        time.sleep(3)

