# Gazstao GzCam
import cv2
import curses
from datetime import datetime

print ("Gazstao (f) 2019-12-22 12h - GzCam")
escala = 2
inverte = False
gray = False
recording = False
diferencial = False
persistencia = False
flip = True
timelapse = False

# captura de vídeo
video = cv2.VideoCapture(0)
frame_num = 0
frame_pers = 0

check, frame_bg = video.read()

# OSD
v = 0
h = 0

# Cria a janela de exibicao
nomeJanela = "Video {}x{}".format( frame_bg.shape[1] , frame_bg.shape[0])
cv2.namedWindow(nomeJanela)
cv2.moveWindow(nomeJanela, 0, 0)

# Prepara a gravação do arquivo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter("GzCam.mp4", fourcc, 15.0, (frame_bg.shape[1], frame_bg.shape[0]))
video_writer_show = cv2.VideoWriter("GazstaoRAW.mp4", fourcc, 15.0, (int(frame_bg.shape[1]/escala),int (frame_bg.shape[0]/escala)))

while True:

    # le o video
    check, frame = video.read()

    # Verifica se alguma tecla foi pressionada
    if timelapse:
        key = cv2.waitKey(200)
    else:
        key = cv2.waitKey(1)

    if key == ord('q'):
        break

    if key == ord('r'):
        if recording:
            recording = False
        else:
            recording = True

    if key == ord('f'):
        if flip: 
            flip = False
        else:
            flip = True

    if key == ord('n'):
        if inverte:
            inverte = False
        else:
            inverte = True
    
    if key == ord('g'):
        if gray:
            gray = False
        else:
            gray = True

    if key == ord('d'):
        if diferencial:
            diferencial = False
        else:
            frame_bg = frame
            diferencial = True
    
    if key == ord('p'):
        if persistencia:
            persistencia = False
        else:
            frame_persistencia  = cv2.absdiff(frame, frame_bg)
            persistencia = True

    if key == ord('t'):
        if timelapse:
            timelapse = False
        else:
            timelapse = True

    if key == ord(' '):
        frame_bg = frame

    if key == ord('l'):
        v = v - 5
    if key == ord('.'):
        v = v + 5
    if key == ord(','):
        h = h - 5
    if key == ord('/'):
        h = h + 5

    # Passa os efeitos de vídeo
    if persistencia:
        frame_pers = frame_pers+1
        if frame_pers == 10:
            frame_persistencia = cv2.absdiff(frame, frame_persistencia)
            frame_pers = 0
        frame  = cv2.absdiff(frame, frame_persistencia)
    if diferencial:
        frame = cv2.absdiff(frame, frame_bg)
    if inverte:
        frame = cv2.bitwise_not(frame)
    if gray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if flip:
        frame = cv2.flip(frame,1)

    # Marca de agua
    #if frame_num <100:
    data = datetime.now()
    frame = cv2.putText(frame,"GzCam 2019 (f) by GAZSTAO   Frame:{} em {}/{}/{}  {}:{}:{}.{}".format(frame_num, data.year, data.month, data.day, data.hour, data.minute, data.second, data.microsecond), (10,30),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
    
    # Se estiver gravando, grava o frame
    if recording:
        frame_num = frame_num + 1
        video_writer.write(frame)  # escreve o frame 

    # Mensagens de efeitos de vídeo
    if inverte:
        frame = cv2.putText(frame,"Negativo", (20+h,20+v),cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
    if gray:
        frame = cv2.putText(frame,"GrayScale", (20+h,40+v), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
    if diferencial:
        frame = cv2.putText(frame,"Diferencial", (20+h,60+v), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
    if persistencia:
        frame = cv2.putText(frame,"Persistencia", (20+h,80+v), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
    if timelapse:
        frame = cv2.putText(frame,"TimeLapse", (20+h,100+v), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
    
    if recording:
        frame = cv2.putText(frame,"Gravando", (20+h,120+v), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255),1)
        # Pisca REC na tela 
        segundos = data.second
        if (segundos%2==0):
            frame = cv2.circle(frame,(10+h,115+v),4,(0,0,255),4)

    # Mostra um frame redimensionado
    frame_resized = cv2.resize(frame, (int (frame.shape[1]/ escala), int (frame.shape[0]/escala) ))
    video_writer_show.write(frame_resized)
    cv2.imshow(nomeJanela,frame_resized)


video.release()
video_writer.release()
video_writer_show.release()
cv2.destroyAllWindows()