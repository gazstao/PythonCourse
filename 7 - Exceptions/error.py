def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Não existe divisão por zero."

print("\n\nExceptions Python Course - Gazstao (f) 2019-11-22\n")
print(dividir(1,1))
print(dividir(1,0))
print("\nThe End!\n")