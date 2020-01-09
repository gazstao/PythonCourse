import cv2
print("\nfaceDetect Gazstao (f) 2019 - Python Course - 2019-12-18 \n")
working_dir = "/Users/gazstao/Google Drive/Programacao/Curso Python/11 - ImageDetection/"

faceCascade = cv2.CascadeClassifier(working_dir+"frontalface_default.xml")
# img = cv2.imread(working_dir+"news.jpg")
img = cv2.imread(working_dir+"photo.jpg")

gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray_image, scaleFactor = 1.15, minNeighbors = 5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+w),(0,255,0), 3)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("faceDetect in Python by Gazs",resized)
cv2.waitKey(10000)
cv2.destroyAllWindows()


