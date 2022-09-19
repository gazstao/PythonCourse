#!/usr/bin/env python3
M = [ [1,2,3] , [4,5,6] , [7,8,9] ]

print(M)
for linha in range(len(M)):
    #print("Linha:",linha," - ",M[linha])
    for coluna in range (len(M[linha])):
        M[linha][coluna]  /= 2

print(M)

Lista = ['Gazstao', 'Gastolino Ferreira' , 'Pasthonild', 'Gaz', 'Bym']

print(Lista)
