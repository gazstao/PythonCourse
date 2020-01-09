import cv2, time
working_dir = "/Users/gazstao/Google Drive/Programacao/Curso Python/11 - ImageDetection/"

print("\nCameraOn VideoCapture in Python by Gazstao (f) 2019-12-19 13h\n")

faceCascade = cv2.CascadeClassifier(working_dir+"frontalface_default.xml")

print("Camera ligada...")
video = cv2.VideoCapture(0)
a=0

while True:
    check, frame = video.read()
    a+=1

    # print(frame) # mostra o numPy das imagens
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # Para ficar preto e branco
    faces = faceCascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 10)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y),(x+w,y+w),(0,255,0), 3)

    fliped = cv2.flip(frame,1) # inverte horizontalmente
    resized = cv2.resize(fliped, (int(fliped.shape[1]/2), int(fliped.shape[0]/2)))
    cv2.imshow("Capturando imagem: {}x{}".format(frame.shape[1],frame.shape[0], a), resized)

    print("Frame: {}".format(a))
    key = cv2.waitKey(50)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print("Camera desligada.")