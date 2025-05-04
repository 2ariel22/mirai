import requests
import time
from Microphone import Microphone

# URL del servidor para enviar texto
SERVER_TEXT_URL = 'http://127.0.0.1:9999/text'
# URL del servidor para enviar audio (opcional)
SERVER_AUDIO_URL = 'http://127.0.0.1:9999/audio'

def main():
    # Inicializar el micrófono
    microfono = Microphone()
    
    print("Presiona Enter para grabar audio o 'q' para salir")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() == 'q':
            print("Saliendo del programa...")
            break
        
        # Grabar audio desde el micrófono
        print("Habla ahora...")
        microfono.grabar_audio()
        
        # Procesar el audio y convertirlo a texto
        texto_detectado = microfono.procesar_audio()
        
        if texto_detectado:
            print(f"Texto detectado: {texto_detectado}")
            
            # Enviar el texto al servidor
            response = requests.post(
                SERVER_TEXT_URL,
                data={'texto': texto_detectado}
            )
            
            print(f"Texto enviado. Código de respuesta: {response.status_code}")
            
            # Si deseas, también puedes enviar el archivo de audio
            """
            with open(microfono.ruta_archivo, 'rb') as audio_file:
                audio_response = requests.post(
                    SERVER_AUDIO_URL,
                    files={'audio': audio_file}
                )
                print(f"Audio enviado. Código de respuesta: {audio_response.status_code}")
            """
        else:
            print("No se detectó texto. No se envió nada al servidor.")

if __name__ == "__main__":
    main()