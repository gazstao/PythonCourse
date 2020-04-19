import time
import os
import pandas

nomearquivo = "Arquivos/TA_PRECO_MEDICAMENTO.csv" 

if os.path.exists("nomearquivo"):
    print("\nArquivo existe!")
print("\nAbrindo arquivo: {}".format(nomearquivo))
with open(nomearquivo, "r",encoding='ISO-8859-1') as dados
    item = dados.read()

print (len(item))
#print(item)
#print(sorted(item))

# outro modo
with open(nomearquivo,  "r",encoding='ISO-8859-1') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.splitlines()

print(len(lista))
listaordenada = sorted(lista)

with open("Arquivos/PrecoOrdenado.TXT","w") as arquivo:
    for item in listaordenada:
        arquivo.write("{}\n\n".format(item))

for i in listaordenada:
    print("\n{}".format(i))
    time.sleep(.05)
