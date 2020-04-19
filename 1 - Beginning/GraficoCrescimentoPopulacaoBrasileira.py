# Crescimento da População Brasileira 1980-2016 - DataSus

# Biblioteca de Graficos
import matplotlib.pyplot as plt

# Acessando Dados do Google Drive
#from google.colab import drive
#from google.colab import files
#drive.mount('/content/drive/', force_remount=True)
dados = open("populacao-brasileira.csv").readlines()

# Carregando os Vetores
x=[]
y=[]

# range cria uma lista que vai de zero até tanto e quer ignorar a primeira linha, linha 0
# coletando os dados
for i in range(len(dados)):
  if i != 0: 
    linha = dados[i].split(";")
    x.append(int(linha[0]))
    y.append(int(linha[1]))

# criando o gráfico
plt.bar(x,y, color="grey")
plt.plot(x,y, color="black",linestyle="--")
# plt.scatter (x, y, marker= "*")

plt.title("Crescimento da População Brasileira de 1980 a 2016")
plt.xlabel("Ano")
plt.ylabel("População *100 milhões")
plt.savefig("populacao_brasileira.png")

plt.show()

#files.download("/content/drive/My Drive/Colab Notebooks/populacao_brasileira.pdf")
