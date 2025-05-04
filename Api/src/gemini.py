import requests


API_KEY = "AIzaSyBgtrCFS9RhUBSW54tu91TQRmItX_IkI9o"  # Reemplázala con tu clave real
class processImg():
    def __init__(self):
        self.imgPath = None
        self.url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
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
