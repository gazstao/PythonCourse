#!/usr/bin/env python3
print("\nRadioactivity (c) 2020 - Gazstao\n")
precisao = 5

meiavida = input("Digite a meia vida do material em qualquer unidade (enter = 6)")
if (meiavida == ""):
    meiavida = 6.0
else:
    meiavida = float(meiavida)

tempodecorrido = input("Tempo decorrido na mesma unidade (enter = 360)")
if (tempodecorrido == ""):
    tempodecorrido = 360;
else:
    tempodecorrido = float(tempodecorrido)

doseinicial = input("Dose inicial em qualquer unidade (Enter ou 100 para calculo em percentual)")
if (doseinicial == ""):
    doseinicial = 100.0
else:
    doseinicial = float(doseinicial)

mvd = tempodecorrido/meiavida
print("\nTotal de meias vidas decorridas: ", mvd)

for x in range (int(tempodecorrido+1)):
    mvd = x/meiavida
    doserestante = doseinicial/(2**mvd)
    print("Tempo decorrido: {} - Dose restante: {} - Meias vidas decorridas: {}".format(x, round(doserestante,precisao+1), round(mvd,2)))
    if (round(doserestante,precisao)==0.0):
        break
