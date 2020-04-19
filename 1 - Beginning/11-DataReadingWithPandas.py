import pandas

htmlcode = { "ó":"&oacute;", "Ó":"&Oacute;" , "á":"&aacute;", "Á":"&Aacute;","é":"&eacute;","É":"&Eacute;",
"ç":"&ccedil","Ç":"&Ccedil;","Â":"&Acirc;","â":"&acirc;","Ã":"&Atilde;","ã":"&atilde;","ê":"&ecirc;",
"Ê":"&Ecirc;","ú":"&uacute;","Ú":"&Uacute;"}

print("\nIniciando the Python Code")
arquivoentrada = "Arquivos/TA_PRECO_MEDICAMENTO.csv"
arquivosaida = "Arquivos/PrecoOrdenado.html"

print("Lendo arquivo {}".format(arquivoentrada))
data = pandas.read_csv(arquivoentrada, "r" , encoding='ISO-8859-1', delimiter=";",low_memory=False)
print("Criando HTML - A conversão pode durar algum tempo... ")
html = pandas.DataFrame.to_html(data)

for key,value in htmlcode.items():
    print("Substituindo {} por {}".format(key,value))
    html = html.replace(key,value)

print("Gravando arquivo: {}".format(arquivosaida))
with open(arquivosaida,"w") as arquivo:  
    arquivo.write(html)
    arquivo.close()

print("Tudo pronto, meu amo!\n")