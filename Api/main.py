from flask import Flask, request
import cv2
import numpy as np
import os
from datetime import datetime
from src.DescribeImg import DescribeImg
import base64
from src.Shadai import ShadaiQueryRunner

app = Flask(__name__)

# Inicializar el sistema de consultas
shadai = ShadaiQueryRunner()

# Directorio para guardar transcripciones de texto (opcional)
SAVE_FOLDER = "text_logs/"
os.makedirs(SAVE_FOLDER, exist_ok=True)




describe = DescribeImg()

@app.route('/img', methods=['POST'])
def receive_frame():
    text = request.form.get('texto')
    print(text)
    file = request.files['frame']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Codificar la imagen como JPG
    _, buffer = cv2.imencode('.jpg', frame)
    encoded_image = base64.b64encode(buffer).decode("utf-8")
    describe.procesar_imagen(encoded_image,text)

    # Guardar imagen con timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S%f')
    filename = f"frame_{timestamp}.jpg"
    filepath = os.path.join(SAVE_FOLDER, filename)
    cv2.imwrite(filepath, frame)

    return "OK", 200

@app.route('/text', methods=['POST'])
def receive_text():
    # Obtener el texto del formulario
    text = request.form.get('texto')
    print(f"Texto recibido: {text}")
    
    # Procesar el texto con el sistema de consultas
    response = shadai.query(text)
    print(f"Respuesta generada: {response}")
    
   
    
    
    
    return "OK", 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)