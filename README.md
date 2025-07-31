<h1 align="center">Mirai - Asistente Visual con IA</h1>

<h2 align="center"><img src="https://img.freepik.com/free-vector/artificial-intelligence-concept-illustration_114360-7000.jpg" width="400"></h2>

<h3 align="center">Introducción</h3>
<p>Mirai es un sistema de asistencia inteligente diseñado para personas con discapacidad visual que utiliza inteligencia artificial para describir el entorno en tiempo real. El proyecto combina tecnologías de visión por computadora, procesamiento de lenguaje natural y síntesis de voz para crear una experiencia accesible e interactiva. El sistema captura imágenes del entorno mediante una cámara, las procesa utilizando la API de Gemini de Google, y proporciona descripciones detalladas y contextuales a través de síntesis de voz en español. Además, incluye funcionalidades de reconocimiento de voz para interacción bidireccional y un sistema de consultas inteligentes para asistencia personalizada.</p>

## :hammer: Funcionalidades del proyecto<br>

### Funcionalidad 1: Descripción Visual del Entorno<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/computer-vision-concept-illustration_114360-7001.jpg">
  <p>El sistema captura imágenes en tiempo real y las procesa con la API de Gemini para generar descripciones detalladas del entorno, objetos y situaciones que se presentan ante la cámara.</p>
</div><br><br>

### Funcionalidad 2: Interacción por Voz<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/voice-recognition-concept-illustration_114360-7002.jpg">
  <p>Permite a los usuarios hacer preguntas específicas sobre lo que ven, recibiendo respuestas personalizadas y contextuales a través de síntesis de voz en español.</p>
</div><br><br>

### Funcionalidad 3: Asistente Inteligente (Shadai)<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/ai-assistant-concept-illustration_114360-7003.jpg">
  <p>Sistema de consultas inteligentes especializado en asistencia a personas con discapacidad, proporcionando respuestas útiles y contextuales a través de voz.</p>
</div><br><br>

### Funcionalidad 4: Registro de Usuarios por Voz<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/accessibility-concept-illustration_114360-7004.jpg">
  <p>Sistema de registro accesible que permite a los usuarios registrarse completamente mediante comandos de voz, incluyendo validación de datos y confirmación auditiva.</p>
</div><br><br>

## 📁 Estructura del Proyecto

### Api/ - Servidor Principal
- **main.py**: Servidor Flask que maneja las peticiones HTTP para procesamiento de imágenes y texto
- **src/DescribeImg.py**: Clase principal para el procesamiento y descripción de imágenes
- **src/gemini.py**: Integración con la API de Gemini para análisis de imágenes
- **src/Shadai.py**: Sistema de consultas inteligentes para asistencia personalizada
- **src/speaker.py**: Sistema de síntesis de voz en español
- **img/**: Directorio de almacenamiento de imágenes capturadas
- **text_logs/**: Registros de consultas y respuestas del sistema

### registerWithVoice/ - Sistema de Registro
- **main.py**: Sistema completo de registro de usuarios mediante voz
- **Microphone.py**: Clase para captura y procesamiento de audio
- **speaker.py**: Sistema de síntesis de voz para confirmaciones

### testingApi/ - Pruebas y Simulación
- **Microphone.py**: Implementación de micrófono para pruebas
- **SImuladorEsp.py**: Simulador para pruebas del sistema
- **simuladorEsp32Shadia.py**: Simulador específico para ESP32

## 🛠️ Tecnologías utilizadas
- **Python 3.12.3**: Lenguaje principal del proyecto
- **Flask**: Framework web para el servidor API
- **OpenCV (cv2)**: Procesamiento de imágenes y captura de video
- **Google Gemini API**: Análisis inteligente de imágenes
- **pyttsx3**: Síntesis de voz en español
- **SpeechRecognition**: Reconocimiento de voz
- **Shadai**: Sistema de consultas inteligentes
- **NumPy**: Procesamiento numérico de imágenes

## :book: Librerías utilizadas
- **flask**: Servidor web y API REST
- **cv2**: Procesamiento de imágenes y video
- **numpy**: Operaciones numéricas
- **requests**: Comunicación HTTP con APIs
- **pyttsx3**: Síntesis de voz
- **speech_recognition**: Reconocimiento de voz
- **python-dotenv**: Manejo de variables de entorno
- **asyncio**: Programación asíncrona
- **threading**: Manejo de hilos
- **datetime**: Manejo de fechas y timestamps
- **base64**: Codificación de imágenes
- **json**: Procesamiento de datos JSON
- **re**: Expresiones regulares para validación

## 📁 Acceso al proyecto

### Para ejecutar el servidor principal:
```bash
cd Api/
python main.py
```

### Para ejecutar el sistema de registro:
```bash
cd registerWithVoice/
python main.py
```

### Para ejecutar las pruebas:
```bash
cd testingApi/
python SImuladorEsp.py
```

## 🛠️ Configuración del proyecto

### 1. Clonar el repositorio:
```bash
git clone https://github.com/2ariel22/mirai.git
cd mirai
```

### 2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 3. Configurar API Key de Gemini:
Crea el archivo `.env` y define la apikey con este nombre `GEMINI_API_KEY` con tu clave real de Google Gemini.

### 4. Configurar el servidor:
El servidor principal se ejecuta en `http://localhost:9999` por defecto.

## 🎯 Casos de Uso

### Descripción del Entorno
El sistema puede describir:
- Objetos y personas en el entorno
- Texto visible en pantallas o documentos
- Colores y formas de objetos
- Distancias y posiciones relativas
- Estados de dispositivos y pantallas

### Asistencia Personalizada
- Respuestas a preguntas específicas sobre el entorno
- Ayuda para navegación y orientación
- Descripción de contenido multimedia
- Asistencia en tareas cotidianas

### Registro Accesible
- Captura de datos personales mediante voz
- Validación automática de información
- Confirmación auditiva de datos
- Interfaz completamente accesible

## 🔧 Endpoints de la API

### POST /img
Procesa imágenes y las describe usando Gemini API
- **Parámetros**: 
  - `frame`: Imagen en formato multipart
  - `texto`: Pregunta o contexto específico

### POST /text
Procesa consultas de texto usando Shadai
- **Parámetros**:
  - `texto`: Consulta o pregunta del usuario

## 📊 Características Técnicas

- **Latencia**: Procesamiento de imágenes en tiempo real
- **Idioma**: Soporte completo para español
- **Accesibilidad**: Interfaz completamente por voz
- **Escalabilidad**: Arquitectura modular y extensible
- **Almacenamiento**: Logs automáticos de consultas e imágenes
- **Seguridad**: Variables de entorno para claves API

## 🔒 Seguridad

### Variables de Entorno
El proyecto utiliza variables de entorno para proteger información sensible como las claves API.

## 🚀 Próximas Funcionalidades

- [ ] Integración con más modelos de IA
- [ ] Soporte para múltiples idiomas
- [ ] Interfaz web accesible
- [ ] Aplicación móvil
- [ ] Integración con dispositivos IoT
- [ ] Sistema de aprendizaje personalizado

## Autores
<div align="center">
  <img src="https://avatars.githubusercontent.com/u/133101799?s=400&u=e9b08cc380e815cf4f929a3f30cb47979d4164f1&v=4" width="115"><br><sub>Ariel Armel Yance Orozco</sub>
</div>

## 📄 Licencia
Este proyecto está desarrollado con fines educativos y de asistencia para personas con discapacidad visual.

## 🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o pull request para sugerir mejoras o reportar problemas. 
