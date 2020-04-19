#from numba import jit, cuda
from datetime import datetime
import numpy as np

print("Gazstao (f) 2019-12-31 00h19")
for i in range (15):
    print("i = {} x 142857 = {}".format(i, i*142857))
for i in range (19):
    print("i = {} x 0588235294117647 = {}".format(i, i*588235294117647))

#calcula pi
#@jit(target ="cuda")

numero = 999999999999999999

def wallis_2(num_fact):
    if (num_fact > 48000000):
        print("Não melhora a precisão após 48 milhões de interações")
        num_fact = 49000000
    mostracada = 1000000
    contador = 1
    acum = np.longdouble(1.0)
    for i in range(1, int(num_fact/2)):
        factor = np.longdouble((2 * i) ** 2) / ((2 * i) ** 2 - 1)
        acum = acum * factor
        if (contador == mostracada):
            data = datetime.now()
            print("{} - interacao {} mi - pi = {}".format(data,i/1000000,2*acum))
            contador = 0
        contador = contador + 1
    return 2 * acum

pi = wallis_2(numero)