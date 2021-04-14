# gazstao 2021-04-12 10h
# Objetivo: carregar os dados JSON obtidos do arquivo para o MongoDB

import json
import pymongo
import sys

print("\n\nGazstao DataParserExperiment 2021-04-13 19h16\n")
#
#       Leitura do arquivo e criação de objeto JSON
#

def file2data():

    arquivo = "/Users/gazstao/github/covid-19-data/public/data/latest/owid-covid-latest.json"
    print("Arquivo :"+arquivo)

    with open(arquivo) as file:
        dados = file.read()

        objeto = json.loads(dados)

        listaDados = []
        for item in objeto:
            listaDados.append(objeto[item])

#
#       Testa conexão ao Mongo e lista Bancos de Dados e Collections
#

def testaMongo(myclient):
    for eachDB in myclient.list_database_names():
        print("\n Banco de Dados:\t {}".format(eachDB))

        mydb = myclient[eachDB]
        for item in mydb.list_collection_names():
            print("    Collection:\t {}".format(item))

#
#       Mongo Conection
#

dbName = "lab05db"
collName = "data05"

try:

    # conecta no mongoDB
    conStr = "mongodb://localhost:27017/"
    myclient = pymongo.MongoClient(conStr)
    print("Cliente criado :{}".format(conStr))
    #testaMongo(myclient)

except:

    print("Erro: {}".format(sys.exc_info()[0]))

prodDB = myclient[dbName]
prodCollection = prodDB[collName]
print(prodCollection.find_one({}))

print("")
