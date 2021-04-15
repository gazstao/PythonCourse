# gazstao 2021-04-12 10h
# Carrega dados JSON obtidos do arquivo para o MongoDB e mostra
# https://github.com/owid/covid-19-data/tree/master/public/data

import json
import pymongo
import sys

conStr = "mongodb://localhost:27017/"
dbName = "DailyData"
collName = "dataref"
arquivo = "/Users/gazstao/github/covid-19-data/public/data/latest/owid-covid-latest.json"
#arquivo = "Data-2021-04-13.json"

print("\n\n\n\n\n\n\nGazstao DataParserExperiment v0.06 2021-04-15 9h09")


#
#       Grava Arquivo JSON único para cada file2data
#

def gravaJSONFile(dados):

        global collName
        jsonData = json.loads(dados)
        for item in jsonData:
            if (item == "OWID_WRL"):
                dataref = jsonData[item]["last_updated_date"]
                f = open("Data-"+dataref+".json", "w")
                f.write(dados)
                f.close()
                print("Arquivo Data-"+dataref+".json criado")
                collName = "{}-{}".format(collName, dataref)


#
#       Leitura do arquivo e criação de objeto JSON
#

def file2data(arquivo):

    with open(arquivo) as file:

        try:
            dados = file.read()
            print("\nArquivo {} carregado com sucesso!".format(arquivo))
            gravaJSONFile(dados)
            return dados

        except:
            print("Não foi possível carregar os dados. Erro: {}".format(sys.exc_info()[0]))



#
#     Lista dados
#

def listaDados(dados):

    qty = 0
    lista = json.loads(dados)
    for item in lista:
        qty += 1
        print("{}){}".format(item, lista[item]["location"]), end="\t\t\t\t")

        if (qty%3 == 0):
            print("") # pula linha

    print ("A lista tem {} itens.".format(qty))
    return lista


#
#       Função insere dados
#

def insereDados(dados, dbConn):

    listaJSON = json.loads(dados)
    for item in listaJSON:

        objID = dbConn.insert_one(listaJSON[item]).inserted_id

        print(json.dumps(item),end=" ")
        print("Objeto {} inserido com sucesso.".format(objID))

#
#       Testa conexão ao Mongo e lista Bancos de Dados e Collections
#

def testaMongo(myclient):

    for eachDB in myclient.list_database_names():
        mydb = myclient[eachDB]

        for item in mydb.list_collection_names():
            print("\t{}:{}".format(eachDB,item))

#
#       Mongo Conection
#

def conectaMongoDB(connectionString):

    try:
        myclient = pymongo.MongoClient(connectionString)
        print("\nConectado :{}".format(connectionString))
        return myclient

    except:
        print("Erro: {}".format(sys.exc_info()[0]))


#
#   EL PROGRAMO
#

dados = file2data(arquivo)

resposta = input ("\nDeseja carregar os dados para o Banco de Dados?\t")
if (resposta == "y" or resposta == "Y" or resposta == "s" or resposta == "S" or resposta == ""):

    nomeDB = input("Nome do Banco de Dados (Enter para usar o padrao "+dbName+"): ")
    if (nomeDB == ""):
        nomeDB = dbName

    nomeCol = input("Nome da Collections (Enter para usar o padrao "+collName+"): ")
    if (nomeCol == ""):
        nomeCol = collName

    adiciona = True
    try:
        cliente = conectaMongoDB(conStr)
        testaMongo(cliente)
        prodDB = cliente[dbName]
        prodCollection = prodDB[collName]
        for item in prodDB.list_collection_names():
            if (item == collName):
                resposta = input("Já existe uma coleção com esse nome. Adicionar mesmo assim? ")
                if (resposta == "y" or resposta == "Y" or resposta == "s" or resposta == "S"):
                    adiciona = True
                else:
                    adiciona = False

    except:
        print("Não foi possível carregar os dados. Erro: {}".format(sys.exc_info()[0]))

    if (adiciona):
        print("Carregando dados para {}".format(prodCollection))
        insereDados(dados, prodCollection)

resposta = input ("\nDeseja visualizar os dados?\t")
if (resposta == "y" or resposta == "Y" or resposta == "s" or resposta == "S" or resposta == ""):
    repete = True
    dadosJSON = listaDados(dados)
else:
    repete = False

while repete:
    item = input ("\nDeseja ver quais informações? ")
    if (item == "exit"):
        repete = False
    else:
        if (item == "" or item == "?"):
            dadosJSON = listaDados(dados)
            print("Digite exit para sair")
        else:
            try:
                print(json.dumps(dadosJSON[item], indent = 4, sort_keys = True))
            except:
                print("Não foi possível carregar os dados. Erro: {}".format(sys.exc_info()[0]))

print("")
