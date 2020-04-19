#from numba import jit, cuda
from datetime import datetime

print("Gazstao (f) 2019-12-31 00h19")
for i in range (15):
    print("i = {} x 142857 = {}".format(i, i*142857))
for i in range (19):
    print("i = {} x 0588235294117647 = {}".format(i, i*588235294117647))

#calcula pi
#@jit(target ="cuda")

numero = 999999999999999999

def wallis_2(num_fact):

    mostracada = 1000000
    contador = 1

    acum = 1.0
    for i in range(1, int(num_fact/2)):
        factor = float((2 * i) ** 2) / ((2 * i) ** 2 - 1)
        acum = acum * factor
        if (contador == mostracada):
            data = datetime.now()
            print("{} - interacao {} - pi = {}".format(data,i,2*acum))
            contador = 0
        contador = contador + 1
    return 2 * acum

pi = wallis_2(numero)