# gazstao 2021-04-12 20h37

import json
arquivo = "/Users/gazstao/github/covid-19-data/public/data/latest/owid-covid-latest.json"
print("\n\nGazstao DataParserExperiment 2021-04-12\nArquivo :"+arquivo)

with open(arquivo) as file:
    dados = file.read()

objeto = json.loads(dados)
listaDados = []

for item in objeto:
#    resposta = input ("Mostrar "+item+" ? ")
#    if (resposta == "y" or resposta == "Y"):
         listaDados.append(objeto[item])
