import pyttsx3
import queue
import speech_recognition as sr
from typing import Optional, Dict, Any
import re
import requests
import json
import time
import threading

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        # Configurar voz en español
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "spanish" in voice.id.lower():
                self.engine.setProperty('voice', voice.id)
                break
    
    def speak(self, texto: str):
        self.engine.say(texto)
        self.engine.runAndWait()

class Microphone:
    def __init__(self):
        self.audio_queue = queue.Queue()
        self.recognizer = sr.Recognizer()
        # Ajustar el nivel de energía para mejorar la detección de voz
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
   
    def grabar_audio(self):
        with sr.Microphone() as source:
            print("\nEscuchando...")
            try:
                # Ajustar para ruido ambiental
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                self.audio_queue.put(audio)
                print("Audio grabado")
            except sr.WaitTimeoutError:
                print("No se detectó audio")
                return False
        return True
            
    def procesar_audio(self) -> Optional[str]:
        try:
            audio = self.audio_queue.get_nowait()
            texto = self.recognizer.recognize_google(audio, language="es-MX")
            print(f"\nHas dicho: {texto}")
            return texto
        except queue.Empty:
            return None
        except sr.UnknownValueError:
            print("\nNo pude entender el audio")
            return None
        except sr.RequestError as e:
            print(f"\nError en el servicio de reconocimiento: {e}")
            return None

class RegistroUsuario:
    def __init__(self):
        self.speaker = Speaker()
        self.microphone = Microphone()
        # Datos a recopilar
        self.datos_usuario = {
            'nombre': None,
            'apellido': None, 
            'correo': None,
            'tipo_usuario': None,
            'tipo_ceguera': None,
            'nombre_contacto': None,
            'telefono_contacto': None
        }
        # Opciones válidas para campos específicos
        self.tipos_ceguera = ['ceguera total', 'baja visión', 'visión periférica']
        self.tipos_usuario = ['paciente', 'familiar', 'médico', 'cuidador']  # Ejemplo de tipos

    def validar_correo(self, correo: str) -> bool:
        # Patrón básico para validar correo electrónico
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron, correo))
    
    def validar_telefono(self, telefono: str) -> bool:
        # Eliminar espacios y caracteres no numéricos
        telefono_limpio = re.sub(r'\D', '', telefono)
        # Verificar que sea un número de 10 dígitos (formato mexicano)
        return len(telefono_limpio) == 10

    def obtener_con_voz(self, campo: str, validacion=None, opciones=None) -> str:
        max_intentos = 4
        intentos = 0
        
        while intentos < max_intentos:
            self.speaker.speak(f"Por favor, diga su {campo}")
            print(f"Esperando {campo}...")
            
            if not self.microphone.grabar_audio():
                self.speaker.speak("No detecté su voz. Intentemos de nuevo.")
                intentos += 1
                continue
                
            time.sleep(0.5)  # Esperar a que el audio esté disponible
            resultado = self.microphone.procesar_audio()
            
            
            if resultado is None:
                self.speaker.speak(f"No pude entender. Intentemos de nuevo con el {campo}.")
                intentos += 1
                continue
            
            # Si hay opciones válidas, verificar que la respuesta esté entre ellas
            if opciones:
                encontrado = False
                for opcion in opciones:
                    if opcion.lower() in resultado.lower():
                        resultado = opcion  # Usar la opción exacta
                        encontrado = True
                        break
                
                if not encontrado:
                    opciones_str = ", ".join(opciones)
                    self.speaker.speak(f"La opción no es válida. Las opciones son: {opciones_str}. Intentemos de nuevo.")
                    intentos += 1
                    continue
            
            # Si hay una función de validación, usarla
            if validacion and not validacion(resultado):
                self.speaker.speak(f"El {campo} proporcionado no es válido. Intentemos de nuevo.")
                intentos += 1
                continue
                
            # Confirmar el dato
            self.speaker.speak(f"He entendido: {resultado}. ¿Es correcto? Diga sí o no.")
            print("Esperando confirmación...")
            
            if not self.microphone.grabar_audio():
                self.speaker.speak("No detecté su respuesta. Intentemos de nuevo.")
                continue
                
            time.sleep(0.5)
            confirmacion = self.microphone.procesar_audio()
            
            if confirmacion and ('sí' in confirmacion.lower() or 'si' in confirmacion.lower()):
                return resultado
            else:
                self.speaker.speak("Entendido, intentemos de nuevo.")
                intentos += 1
        
        self.speaker.speak(f"Ha superado el número máximo de intentos para {campo}. Por favor, intente más tarde o contacte a soporte.")
        return None

    def iniciar_registro(self):
        self.speaker.speak("Bienvenido al sistema de registro de usuarios. Vamos a pedirle algunos datos.")
        
        # Obtener nombre
        self.datos_usuario['nombre'] = self.obtener_con_voz("nombre")
        if not self.datos_usuario['nombre']:
            return False
            
        # Obtener apellido
        self.datos_usuario['apellido'] = self.obtener_con_voz("apellido")
        if not self.datos_usuario['apellido']:
            return False
            
        # Obtener correo con validación
        self.datos_usuario['correo'] = self.obtener_con_voz("correo electrónico", self.validar_correo)
        if not self.datos_usuario['correo']:
            return False
            
        # Obtener tipo de usuario con opciones
        self.datos_usuario['tipo_usuario'] = self.obtener_con_voz("tipo de usuario", opciones=self.tipos_usuario)
        if not self.datos_usuario['tipo_usuario']:
            return False
            
        # Obtener tipo de ceguera con opciones
        self.datos_usuario['tipo_ceguera'] = self.obtener_con_voz("tipo de ceguera", opciones=self.tipos_ceguera)
        if not self.datos_usuario['tipo_ceguera']:
            return False
            
        # Obtener nombre de contacto
        self.datos_usuario['nombre_contacto'] = self.obtener_con_voz("nombre de contacto")
        if not self.datos_usuario['nombre_contacto']:
            return False
            
        # Obtener teléfono de contacto con validación
        self.datos_usuario['telefono_contacto'] = self.obtener_con_voz("teléfono de contacto", self.validar_telefono)
        if not self.datos_usuario['telefono_contacto']:
            return False
            
        return True

    def enviar_a_api(self) -> bool:
        """
        Envía los datos recopilados a la API
        """
        try:
            # URL de ejemplo - reemplazar con la URL real de tu API
            url = "https://tu-api.com/registrar-usuario"
            
            # Asegurarse de que el número de teléfono sea solo números
            if self.datos_usuario['telefono_contacto']:
                self.datos_usuario['telefono_contacto'] = re.sub(r'\D', '', self.datos_usuario['telefono_contacto'])
            
            # Convertir datos a JSON
            payload = json.dumps(self.datos_usuario)
            headers = {
                'Content-Type': 'application/json'
            }
            
            # Simular el envío a la API (comentar y usar el código real cuando sea necesario)
            print(f"Enviando datos a la API: {payload}")
            
            # Para implementación real:
            # response = requests.post(url, data=payload, headers=headers)
            # return response.status_code == 200
            
            # Simulación:
            return True
            
        except Exception as e:
            print(f"Error al enviar datos: {e}")
            return False

    def ejecutar(self):
        """
        Método principal para ejecutar todo el proceso de registro
        """
        self.speaker.speak("Iniciando sistema de registro por voz.")
        
        if self.iniciar_registro():
            self.speaker.speak("Registro completado. Enviando datos al sistema.")
            if self.enviar_a_api():
                self.speaker.speak("Datos enviados correctamente. ¡Registro exitoso!")
                return True
            else:
                self.speaker.speak("Error al enviar los datos. Por favor, inténtelo más tarde.")
                return False
        else:
            self.speaker.speak("El registro no pudo completarse. Por favor, inténtelo más tarde.")
            return False

if __name__ == "__main__":
    registro = RegistroUsuario()
    registro.ejecutar()