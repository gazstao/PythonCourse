import keyboard
import time

print("\n\n\nAztech DOS System 2022.09.14-09h27\n\n")

def menu():
    opcao = 0
    print('1) Consultar')
    print('2) Consultar')
    print('3) Consultar')
    print('4) Consultar')
    print('5) Consultar')
    while opcao == 0:
        if keyboard.is_pressed('1'):
            print(1)
            time.sleep(.1)
        if keyboard.is_pressed('2'):
            print(2)
            time.sleep(.1)
        if keyboard.is_pressed('3'):
            print(3)
            time.sleep(.1)
        if keyboard.is_pressed('4'):
            print(4)
            time.sleep(.1)
        if keyboard.is_pressed('5'):
            print(5)
            time.sleep(.1)

menu()