from src.gemini import processImg
from src.speaker import Speaker
import os


imgPath = "img/20250503214848.jpg"

class DescribeImg():
    def __init__(self):
        self.procesamiento = processImg()
        self.speaker = Speaker()
        

    def procesar_imagen(self, img,text):
        try:
            
            texto = self.procesamiento.process(img,text)
            #print(type(texto))
            
            print("=== Descripción de la imagen ===")
          
            print(f"Descripción: {texto}")
            print("=============================")
            newText = list(texto)[1].replace("\n", "")
            # Leer la descripción en voz alta
            self.speaker.speak(newText)
            
        except Exception as e:
            print(f"Error al procesar la imagen: {str(e)}")

#def main():
    #print("Ininciando Monitor de imagenes")
    #describe = DescribeImg()
    #with open(imgPath, "rb") as image_file:
    #        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    #        describe.procesar_imagen(encoded_image)
          


#if __name__ == '__main__':
 #   main()

