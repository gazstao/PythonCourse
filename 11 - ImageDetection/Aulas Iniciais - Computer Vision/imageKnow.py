import cv2

arquivo = "/Users/gazstao/Google Drive/Programacao/Curso Python/11 - ImageDetection/Aulas Iniciais - Computer Vision/galaxy.jpg" 
img = cv2.imread(arquivo,0) # -1 Color Tranparency / 0 para Grayscale / 1 para Cor
print ("\nGazstao - 2019-12-17 20h\nPython ImageKnowing\n\n")

print("Arquivo carregado: {}".format(arquivo))
print("type(img)= {}".format(type(img)))
print("img = {}".format(img))
print("img.ndim = {}".format(img.ndim))
print("img.shape= {}".format(img.shape))

#resized_img = cv2.resize(img,(1000,800))
resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img)
cv2.waitKey(0) # ou tempo para fechar a janela em ms
cv2 .destroyAllWindows() 