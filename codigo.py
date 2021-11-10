# Biblioteca reconhceimento facial
import cv2

# Função ouvir_microfone

video_capture = cv2.VideoCapture(0)
# Cascades

# Flags

while True:
    ret, frame = video_capture.read()

    teste = cv2.waitKey(1)

    if teste == ord('a'):
        flagOuvir = True
    if teste == ord('q'):
        break

    # Toda a parte do while para reconhecimento facial + voz

    cv2.imshow('video', frame)


#ouvir_microfone()

video_capture.release()
cv2.destroyAllWindows()
