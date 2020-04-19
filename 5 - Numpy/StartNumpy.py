import cv2
im_g=cv2.imread("/Users/gazstao/Downloads/smallgray.png",0)

print(im_g)

opcao = input("\nQualquer tecla para continuar... (S para mostrar matriz)")
if opcao.upper() == "S":
    for i in im_g.flat:
        print("{}  ".format(i),end="")