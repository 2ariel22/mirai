<h1 align="center">Mirai - AI Visual Assistant</h1>

<div align="center">
  <a href="README.md">🇪🇸 Leer en Español</a>
</div>

<h2 align="center"><img src="https://img.freepik.com/free-vector/artificial-intelligence-concept-illustration_114360-7000.jpg" width="400"></h2>

<h3 align="center">Introduction</h3>
<p>Mirai is an intelligent assistance system designed for visually impaired individuals that uses artificial intelligence to describe the environment in real-time. The project combines computer vision technologies, natural language processing, and voice synthesis to create an accessible and interactive experience. The system captures images of the environment through a camera, processes them using Google's Gemini API, and provides detailed and contextual descriptions through Spanish voice synthesis. Additionally, it includes voice recognition functionalities for bidirectional interaction and an intelligent query system for personalized assistance.</p>

## :hammer: Project Features<br>

### Feature 1: Visual Environment Description<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/computer-vision-concept-illustration_114360-7001.jpg">
  <p>The system captures images in real-time and processes them with the Gemini API to generate detailed descriptions of the environment, objects, and situations presented to the camera.</p>
</div><br><br>

### Feature 2: Voice Interaction<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/voice-recognition-concept-illustration_114360-7002.jpg">
  <p>Allows users to ask specific questions about what they see, receiving personalized and contextual responses through Spanish voice synthesis.</p>
</div><br><br>

### Feature 3: Intelligent Assistant (Shadai)<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/ai-assistant-concept-illustration_114360-7003.jpg">
  <p>Intelligent query system specialized in assistance for people with disabilities, providing useful and contextual responses through voice.</p>
</div><br><br>

### Feature 4: Voice User Registration<br>
<div align="center">
  <img width="400" src="https://img.freepik.com/free-vector/accessibility-concept-illustration_114360-7004.jpg">
  <p>Accessible registration system that allows users to register completely through voice commands, including data validation and audio confirmation.</p>
</div><br><br>

## 📁 Project Structure

### Api/ - Main Server
- **main.py**: Flask server that handles HTTP requests for image and text processing
- **src/DescribeImg.py**: Main class for image processing and description
- **src/gemini.py**: Integration with Gemini API for image analysis
- **src/Shadai.py**: Intelligent query system for personalized assistance
- **src/speaker.py**: Spanish voice synthesis system
- **img/**: Directory for storing captured images
- **text_logs/**: System query and response logs

### registerWithVoice/ - Registration System
- **main.py**: Complete user registration system via voice
- **Microphone.py**: Class for audio capture and processing
- **speaker.py**: Voice synthesis system for confirmations

### testingApi/ - Testing and Simulation
- **Microphone.py**: Microphone implementation for testing
- **SImuladorEsp.py**: System testing simulator
- **simuladorEsp32Shadia.py**: ESP32-specific simulator

## 🛠️ Technologies Used
- **Python 3.12.3**: Main project language
- **Flask**: Web framework for the API server
- **OpenCV (cv2)**: Image processing and video capture
- **Google Gemini API**: Intelligent image analysis
- **pyttsx3**: Spanish voice synthesis
- **SpeechRecognition**: Voice recognition
- **Shadai**: Intelligent query system
- **NumPy**: Numerical image processing

## :book: Libraries Used
- **flask**: Web server and REST API
- **cv2**: Image and video processing
- **numpy**: Numerical operations
- **requests**: HTTP communication with APIs
- **pyttsx3**: Voice synthesis
- **speech_recognition**: Voice recognition
- **python-dotenv**: Environment variable management
- **asyncio**: Asynchronous programming
- **threading**: Thread management
- **datetime**: Date and timestamp handling
- **base64**: Image encoding
- **json**: JSON data processing
- **re**: Regular expressions for validation

## 📁 Project Access

### To run the main server:
```bash
cd Api/
python main.py
```

### To run the registration system:
```bash
cd registerWithVoice/
python main.py
```

### To run the tests:
```bash
cd testingApi/
python SImuladorEsp.py
```

## 🛠️ Project Configuration

### 1. Clone the repository:
```bash
git clone <repository-url>
cd mirai
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables:
```bash
# Copy the example file
cp env.example .env

# Edit the .env file with your Gemini API key
# Get your API key at: https://makersuite.google.com/app/apikey
```

### 4. Configure Gemini API Key:
Edit the `.env` file and replace `tu_api_key_de_gemini_aqui` with your real Google Gemini API key.

### 5. Configure the server:
The main server runs on `http://localhost:9999` by default.

## 🎯 Use Cases

### Environment Description
The system can describe:
- Objects and people in the environment
- Text visible on screens or documents
- Colors and shapes of objects
- Relative distances and positions
- Device and screen states

### Personalized Assistance
- Responses to specific questions about the environment
- Help with navigation and orientation
- Description of multimedia content
- Assistance with daily tasks

### Accessible Registration
- Personal data capture through voice
- Automatic information validation
- Audio confirmation of data
- Completely accessible interface

## 🔧 API Endpoints

### POST /img
Processes images and describes them using Gemini API
- **Parameters**: 
  - `frame`: Image in multipart format
  - `texto`: Specific question or context

### POST /text
Processes text queries using Shadai
- **Parameters**:
  - `texto`: User query or question

## 📊 Technical Features

- **Latency**: Real-time image processing
- **Language**: Complete Spanish support
- **Accessibility**: Completely voice-based interface
- **Scalability**: Modular and extensible architecture
- **Storage**: Automatic logs of queries and images
- **Security**: Environment variables for API keys

## 🔒 Security

### Environment Variables
The project uses environment variables to protect sensitive information such as API keys. Never upload `.env` files with real keys to the repository.

### Files to include in .gitignore:
```
.env
*.log
__pycache__/
*.pyc
.DS_Store
```

## 🚀 Upcoming Features

- [ ] Integration with more AI models
- [ ] Multi-language support
- [ ] Accessible web interface
- [ ] Mobile application
- [ ] IoT device integration
- [ ] Personalized learning system

## Authors
<div align="center">
  <img src="https://avatars.githubusercontent.com/u/133101799?s=400&u=e9b08cc380e815cf4f929a3f30cb47979d4164f1&v=4" width="115"><br><sub>Ariel Armel Yance Orozco</sub>
</div>

## 📄 License
This project is developed for educational purposes and assistance for visually impaired individuals.

## 🤝 Contributions
Contributions are welcome. Please open an issue or pull request to suggest improvements or report problems. 