import cv2, time
from datetime import datetime

def atualiza_bg():
    global frame_bg
    global bg_resized
    check, frame_bg = video.read()
    frame_bg = cv2.cvtColor(frame_bg, cv2.COLOR_BGR2GRAY) # frame para escala de cinza
    frame_bg = cv2.flip(frame_bg,1) # flip
    bg_resized = cv2.resize(frame_bg, ( int(frame_bg.shape[1]/escala), int (frame_bg.shape[0]/escala))) # redimensionando
    
print("\nGazstao WebCamMotionDetection - Udemy Python Course - Lesson 26 - 2019-12-19 14h (f) by Gazstao\n")

# captura frame Background e posiciona as janelas
escala = 3 # 1 para x
video = cv2.VideoCapture(0)
recording = True

# Video
frame_num = 0
auto_bg = True
ciclo_bg = 1000

atualiza_bg()

nome_janela = "Grayscale {}x{}".format(frame_bg.shape[1],frame_bg.shape[0])
cv2.namedWindow(nome_janela) # Cria a janela nomeada
cv2.moveWindow(nome_janela, int(frame_bg.shape[1]/escala+30), 0) # Move a janela
cv2.namedWindow("Original")
cv2.moveWindow("Original", 0, int(frame_bg.shape[0]/escala+70))
cv2.namedWindow("Background")
cv2.moveWindow("Background", 0, 0)
cv2.namedWindow("Diferencial")
cv2.moveWindow("Diferencial", int(frame_bg.shape[1]/escala+30), int(frame_bg.shape[0]/escala+70))
cv2.namedWindow("Threshold")
cv2.moveWindow("Threshold", int(frame_bg.shape[1]/escala+30)*2,0 )
cv2.namedWindow("Contorno")
cv2.moveWindow("Contorno", int(frame_bg.shape[1]/escala+30)*2, int(frame_bg.shape[0]/escala+70))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter("delta.mp4", fourcc, 15.0, (frame_bg.shape[1], frame_bg.shape[0]))

while True:

    # Grava o frame
    frame_num = frame_num + 1
    check, frame = video.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # frame para escala de cinza
    gray = cv2.flip(gray,1)  # espelha a imagem
    gray_resized = cv2.resize(gray, (int(gray.shape[1]/escala), int (gray.shape[0]/escala))) 
    gray = cv2.GaussianBlur(gray,(21,21),0) # borra a imagem
    
    delta_frame = cv2.absdiff(frame_bg, gray)
    delta_resized = cv2.resize(delta_frame,( int(gray.shape[1]/escala), int (gray.shape[0]/escala)))

    threshold_delta = cv2.threshold (delta_frame, 30,255, cv2.THRESH_BINARY)[1]
    threshold_delta = cv2.dilate(threshold_delta, None, iterations=2)
    threshold_delta_resized = cv2.resize(threshold_delta,(int(threshold_delta.shape[1]/escala), int (threshold_delta.shape[0]/escala)))

    contorno = cv2.flip(frame,1)
    (cnts, _) = cv2.findContours(threshold_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 5000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(contorno, (x,y), (x+w, y+h), (0,255,0), 3)
    contorno_resized = cv2.resize(contorno,(int(contorno.shape[1]/escala), int (contorno.shape[0]/escala))) 
    original_resized = cv2.resize(frame, (int (frame.shape[1]/escala), int (frame.shape[0]/escala) ))

    if recording:
        data = datetime.now()
        segundos = data.second
        if (segundos%2==0):
            contorno_resized = cv2.circle(contorno_resized,(20,20),3,(0,0,255),3)
        if check:
            video_writer.write(cv2.cvtColor(delta_frame, cv2.COLOR_RGB2BGR))

    cv2.imshow(nome_janela , gray_resized)
    cv2.imshow("Original",original_resized)
    cv2.imshow("Diferencial", delta_resized)
    cv2.imshow("Threshold", threshold_delta_resized)
    cv2.imshow("Background", bg_resized)
    cv2.imshow("Contorno", contorno_resized)
   
    key = cv2.waitKey(5)

    if key==ord('r'):
        if recording:
            recording = False
        else:
            recording = True

    if key==ord('q'):
        break

    # Espaço para "resetar" o frame_bg
    if key==ord(' '):
        atualiza_bg()
      
    if auto_bg:
        if ( (frame_num%ciclo_bg) == 0):
            atualiza_bg()

video.release()
video_writer.release()
cv2.destroyAllWindows()
print("Programa terminado após {} frames.\n".format(frame_num))