import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class processImg():
    def __init__(self):
        self.imgPath = None
        self.api_key = os.getenv('GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY no está configurada en las variables de entorno")
        self.url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={self.api_key}"
    def process(self, img, text):

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [{
                "parts": [
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": img
                        }
                    },
                    {
                        "text": f"Describe de forma clara y precisa esta imagen para una persona con ceguera, enfocándote específicamente en lo que se solicita a continuación. No incluyas saludos, decoraciones ni saltos de línea ('\\n'). Responde únicamente con una descripción en un solo párrafo de máximo cuatro renglones. Asegúrate de atender y resaltar lo que el usuario pide: {text}"

                    }
                ]
            }]
        }

        # Enviar la solicitud
        response = requests.post(self.url, headers=headers, json=data)

        # Mostrar la respuesta
        if response.status_code == 200:
            result = response.json()
            return ("Descripción:", result["candidates"][0]["content"]["parts"][0]["text"])
        else:
            return("Error:", response.status_code, response.text)
