print("\n\nWelcome to the Python Dictionary!")
print("by Gazstao 2019 - Unity - Ardit Soulce")

bestmatches = 7 # similar matches

import json #biblioteca para arquivos Json
import difflib #biblioteca para comparação de arquivos

data = json.load(open("/Users/gazstao/Documents/Curso Python/2 - English Dictionary/Arquivos/data.json"))

def traduza(palavra):
    if palavra.casefold() in data:
        return data[palavra.casefold()]
    elif palavra.title() in data:
        return data[palavra.title()]
    elif palavra in data:
        return data[palavra]
    else:
        similares = difflib.get_close_matches(palavra,data.keys(), bestmatches)
        lista = ""
        for i in range(len(similares)):
            if i == 0:
                lista = similares[i]
            else:
                lista = "{}, {}".format(lista, similares[i])
        return "Sorry!! Never hear about it ...  :(\nSimilar known words: {}.".format(lista)

while True:
    palavra = input("\nTell me a word: ")
    if palavra.upper() == "\END" or palavra.upper() == "QUIT()" or palavra=="":
        print("\nThank you for using me!")
        break
    else:
        print("\n{}".format(palavra))
        traducao = traduza(palavra)
        x=1
        if type(traducao) == list:
            for elementos in traduza(palavra):
                print("{}) {}".format(x,elementos))
                x+=1
        else:
            print(traducao)