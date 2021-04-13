# gazstao 2021-04-12 10h
# Objetivo: carregar os dados JSON obtidos do arquivo para o MongoDB

import json
import pymongo
import sys

#
#       Leitura do arquivo e criação de objeto JSON
#

def file2data():

    arquivo = "/Users/gazstao/github/covid-19-data/public/data/latest/owid-covid-latest.json"
    print("\n\nGazstao DataParserExperiment 2021-04-13\nArquivo :"+arquivo)

    with open(arquivo) as file:
        dados = file.read()

        objeto = json.loads(dados)

        listaDados = []
        for item in objeto:
            listaDados.append(objeto[item])

#
#       Mongo Conection
#

dbName = "lab05db"
conStr = "mongodb://localhost:27017/"

try:
    myclient = pymongo.MongoClient(conStr)
    print("Cliente criado...")
    print("Bancos de Dados encontrados :")
    for eachDB in myclient.list_database_names():
        print("  {}".format(eachDB))
    mydb = myclient[dbName]
    print("Conectado em {}".format(dbName))

except:
    print("Não foi possível conectar ao banco de dados {} em {}".format(dbName, conStr))
    print("Erro: {}".format(sys.exc_info()[0]))

for item in mydb.find():
    print(item)
