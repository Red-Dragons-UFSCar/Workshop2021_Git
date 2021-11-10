import speech_recognition as sr
import cv2

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuário
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #Chama um algoritmo de reducao de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        #Passa a variável para o algoritmo reconhecedor de padroes
        frase = microfone.recognize_google(audio,language='pt-BR')

        #Retorna a frase pronunciada
        print("Você disse: " + frase)

    #Se nao reconheceu o padrao de fala, exibe a mensagem
    except sr.UnkownValueError:
        print("Não entendi")

    return frase

# Declarando os objetos do openCV
video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smileCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Inicialização de Flags para reconhecimento facial
flagOuvir = False
flagDetectFace = False
flagDetectOlho = False
flagDetectBoca = False

while True:
    # Captura da webcam
    ret, frame = video_capture.read()

    # Converter o frame capturado da camera em escalas de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Configuração para reconhecimento facial
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Captura de uma tecla do teclado
    teste = cv2.waitKey(1)

    # Se for 'a', capturar o audio.
    # Se for 'q', fechar a webcam
    if teste == ord('a'):
        flagOuvir = True
    if teste == ord('q'):
        break

    # Se a for apertado
    if flagOuvir:

        # Detecção de audio
        frase = ouvir_microfone()
        frase = frase.lower()
        flagOuvir = False

        # Condições para ligar/desligar reconhecimentos
        if "ligar face" in frase:
            flagDetectFace = True

        if "ligar olho" in frase:
            flagDetectOlho = True

        if "ligar boca" in frase:
            flagDetectBoca = True

        if "desligar face" in frase:
            flagDetectFace = False

        if "desligar olho" in frase:
            flagDetectOlho = False

        if "desligar boca" in frase:
            flagDetectBoca = False

    # Detecção das partes da face
    if flagDetectFace:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if flagDetectOlho:
        eyes = eyeCascade.detectMultiScale(gray, 1.2, 18)
        for (x, y, w, h) in eyes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if flagDetectBoca:
        smiles = smileCascade.detectMultiScale(gray, 1.7, 20)
        for (x, y, w, h) in smiles:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Mostrar vídeo
    cv2.imshow('video', frame)

# Finalizando o código
video_capture.release()
cv2.destroyAllWindows()
