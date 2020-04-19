def mean(*args):
  return sum(args) / len(args)

def mean(args):
  soma = 0
  for i in args:
    soma+=float(i)
  return soma / len(args)
  
lista = (10.0, 5.5, 7.0, 7.5)

print(lista)
print(mean(lista))
#print ("A média de {} é {}".format(lista, mean(lista)))