import turtle
import psutil
import time

from tqdm import tqdm
from time import sleep
import psutil

print("CPUs: {}".format(psutil.cpu_count()))

with tqdm(total=100, desc='cpu%', position=1) as cpubar, tqdm(total=100, desc='ram%', position=0) as rambar:
    while True:
        rambar.n=psutil.virtual_memory().percent
        cpubar.n=psutil.cpu_percent()
        rambar.refresh()
        cpubar.refresh()
        time.sleep(.1)

x = 1400
y = 900

turtle.setup(x,y)
turtle.setposition(-x/2,y/2-100)
turtle.bgcolor('black')
turtle.color('green')
turtle.hideturtle()

for i in range(x):
    turtle.setposition(i-x/2,psutil.cpu_percent()*20-y/2+200)
    time.sleep(.1)
