# Librerias
from colorama import init, Fore, Back, Style
from tqdm import tqdm
from time import sleep
import wikipedia
from gtts import gTTS
import os


# Metodo de busqueda de tema y resumen en wikipedia
print(Fore.RED+"¿Que tema necesitas?")
tema = input()
print(Fore.BLUE+"¿Cuantos parrafos desea?")
parrafos = input()
wikipedia.set_lang("es")

# Barra de carga
busqueda = 100
print(Fore.CYAN+"Buscando...")
for i in tqdm(range(busqueda)):
    sleep(0.02)
print(Fore.GREEN+"----------Resultado encontrado----------")

# Resultado impreso en consola
print(wikipedia.summary(tema, sentences=parrafos))

# Genera archivo de Mp3 con el tema buscado buscado
texto = wikipedia.summary(tema, sentences=parrafos)
lenguaje = 'es'
audio = gTTS(text=texto, lang=lenguaje, slow=False)
audio.save("-resumen.mp3")
print(Fore.RED+"----------El archivo mp3 se abrira enseguida:----------")
# Abrir archivo mp3 generado en reproductor del sistema
os.system("-resumen.mp3")
print(Fore.MAGENTA+"----------Resumen en mp3 generado----------")
