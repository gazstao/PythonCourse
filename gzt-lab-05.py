# gazstao 2021-04-12 10h
# Objetivo: carregar os dados JSON obtidos do arquivo para o MongoDB

import json
import pymongo
import sys

dbName = "gzt-lab"
collName = "data20210414"
arquivo = "/Users/gazstao/github/covid-19-data/public/data/latest/owid-covid-latest.json"

print("\n\nGazstao DataParserExperiment 2021-04-13 19h16\n")
#
#       Leitura do arquivo e criação de objeto JSON
#

def file2data(arquivo):

    print("Arquivo :"+arquivo)

    with open(arquivo) as file:
        dados = file.read()

        objJSON = json.loads(dados)
        return objJSON

#
#       Função Lista Dados
#

def insereDados(objJSON, dbConn):
    for item in objJSON:
        print(json.dumps(item),end=" ")
        # print(json.dumps(objJSON[item], indent = 4, sort_keys = True))
        objID = dbConn.insert_one(objJSON[item]).inserted_id
        print("Objeto {} inserido com sucesso.".format(objID))

#
#       Testa conexão ao Mongo e lista Bancos de Dados e Collections
#

def testaMongo(myclient):
    for eachDB in myclient.list_database_names():
        print("\n Banco de Dados:\t {}".format(eachDB))

        mydb = myclient[eachDB]
        for item in mydb.list_collection_names():
            print("    Collection:\t\t {}".format(item))

#
#       Mongo Conection
#

try:

    # conecta no mongoDB
    conStr = "mongodb://localhost:27017/"
    myclient = pymongo.MongoClient(conStr)
    print("Cliente criado :{}".format(conStr))
    testaMongo(myclient)

except:

    print("Erro: {}".format(sys.exc_info()[0]))


#
#   EL PROGRAMO
#

prodDB = myclient[dbName]
prodCollection = prodDB[collName]

dadosJSON = file2data(arquivo)
insereDados(dadosJSON, prodCollection)

print("")
