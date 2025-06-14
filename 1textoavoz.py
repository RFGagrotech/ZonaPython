#La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible 
#en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de 
#herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de 
#instalación de pip). 
#Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para 
#luego manejar la conversión de texto a voz.

import requests
from bs4 import BeautifulSoup
from gtts import gTTS

# Solicita la URL
url = input("Introduce la URL: ")

# Obtiene el contenido HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extrae los párrafos
paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]

# Muestra los párrafos numerados
for i, para in enumerate(paragraphs):
    print(f"\n[{i}] {para[:200]}{'...' if len(para) > 200 else ''}")

# Selección de párrafos con soporte para múltiples índices y rangos
selection = input("\nIntroduce los números de los párrafos (ej. 1,3 o 1-3): ").replace(" ", "")
selected_texts = []

try:
    parts = selection.split(',')
    for part in parts:
        if '-' in part:
            start, end = map(int, part.split('-'))
            selected_texts.extend(paragraphs[start:end+1])
        else:
            selected_texts.append(paragraphs[int(part)])
except (ValueError, IndexError):
    print("Selección inválida.")
    exit()

# Junta todos los textos seleccionados
selected_text = '\n'.join(selected_texts)

# Solicita el nombre del archivo
file_name = input("Introduce el nombre para el archivo MP3 (sin extensión): ").strip()
file_path = f"{file_name}.mp3"

# Convierte a audio y guarda
tts = gTTS(text=selected_text, lang='es')
tts.save(file_path)
print(f"Archivo '{file_path}' guardado.")

