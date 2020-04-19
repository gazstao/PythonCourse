lista_notas_aluno = [8.0, 7.0, 7.5, 7.5]
dicionario_notas = { "Semestre 1":8.0, "Semestre 2": 7.0, "Semestre 3":7.5, "Semestre 4":7.5 }
tupla_notas = (8.0,7.0,7.5,7.5)
day_temperatures = { "morning" : (14.0, 13.0, 16.0),
                    "noon" : (20.0,23.5, 22.0),
                    "evening" : (13.0, 14.0, 15.0)}

print("day_temperatures.keys&values:")
print (day_temperatures.keys())
print(day_temperatures.values())

soma = sum(lista_notas_aluno)
tamanho = len(lista_notas_aluno)
media = soma/tamanho
print("\nMedia da Lista lista_notas_aluno")
print(media)

soma = sum(dicionario_notas.values())
tamanho = len(lista_notas_aluno)
media = soma/tamanho
print("\nMedia dos Valores do Dicionario Notas")
print(media)

soma = sum(tupla_notas)
tamanho = len(tupla_notas)
media = soma/tamanho
print("\nMedia de tupla_notas")
print(media)

print("\nnotas.values e notas.keys()")
print(dicionario_notas.values())
print(dicionario_notas.keys())

print("\nlista_nota_alunos")
print(lista_notas_aluno)

eng_port = {"rain":"chuva","sun":"sol", "wind":"vento"}
print("\neng_port[\"rain\"]")
print(eng_port["rain"])