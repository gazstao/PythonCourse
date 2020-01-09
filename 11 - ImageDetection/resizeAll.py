import  cv2
import glob

arquivos = "/Users/gazstao/Google Drive/Programacao/Curso Python/11 - ImageDetection/Aulas Iniciais - Computer Vision/sample-images/*.jpg" 
print("Gazstao imgDirResize 2019-12-17 21h")
images = glob.glob(arquivos)

for imagem in images:
    img = cv2.imread(imagem,0)
    resized = cv2.resize(img, (100,100))
    cv2.imshow("ImagemFinal", resized)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("{}_resized.jpg".format(imagem),resized)