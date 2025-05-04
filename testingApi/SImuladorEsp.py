import cv2
import requests
from Microphone import Microphone  # Asegúrate que mic.py contiene la clase Microphone corregida


SERVER_URL = 'http://127.0.0.1:9999/img'
cap = cv2.VideoCapture(0)
microfono = Microphone()


while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Presiona 'k' para grabar y enviar", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('k'):
        print("Habla ahora...")
        microfono.grabar_audio()
        texto_detectado = microfono.procesar_audio()

        if texto_detectado:
            _, jpeg = cv2.imencode('.jpg', frame)
            response = requests.post(
                SERVER_URL,
                files={'frame': jpeg.tobytes()},
                data={'texto': texto_detectado}
            )
            print(f"Imagen y texto enviados. Código: {response.status_code}")
        else:
            print("No se detectó texto. No se envió la imagen.")
        
        # Después de enviar la imagen y el texto, vuelve a esperar la siguiente tecla 'k'

    elif key == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
