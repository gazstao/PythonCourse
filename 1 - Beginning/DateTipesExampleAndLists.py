umaString = "Uma String"
umInt = 10
umFloat = 10.0

notas_aluno = [8.0, 8.8, 7.5, 7.0]
numeros = list(range(0,11))
pares = list(range(0,100,2))
impares = list(range(1,100,2))

print("\nnotas_aluno")
print (notas_aluno)
print("\nnumeros")
print (numeros)
print("\npares")
print (pares)
print("\nimpares")
print (impares)

soma = sum(notas_aluno)
tam = len(notas_aluno)
media = soma/tam
print("\nMedia do Aluno:")
print(media)

# para saber tudo sobre int
# print(dir(int))

print("\npares[:5]")
print(pares[:5])
print("\nimpares[:5]")
print(impares[:5])

print("\npares[-2:]")
print(pares[-2:])
print("\nimpares[-2:]")
print(impares[-2:])

print("\nGazstao (f) 2019\n")