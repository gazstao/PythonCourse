print("\nRadioactivity (c) 2020 - Gazstao\n")

meiavida = float(input("Digite a meia vida do material: "))
tempodecorrido = float(input("Tempo decorrido: "))
doseinicial = float(input("Dose inicial (100 para calculo em percentual): "))

mvd = tempodecorrido/meiavida
print("\nTotal de meias vidas decorridas: ", mvd)

for x in range (int(tempodecorrido+1)):
    mvd = x/meiavida
    doserestante = doseinicial/(2**mvd)
    print("Tempo decorrido: {} - Dose restante: {} - Meias vidas decorridas: {}".format(x, round(doserestante,2), round(mvd,2)))
