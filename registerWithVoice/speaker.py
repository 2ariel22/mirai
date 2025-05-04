import pyttsx3
class Speaker():
    def __init__(self):
       pass
       

    def speak(self, texto: str):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            if "spanish" in voice.id.lower():
                engine.setProperty('voice', voice.id)
                break
        engine.say(texto)
        engine.runAndWait()
        engine.stop()
