#En este proyecto utilizarás el módulo "langdetect" para ayudarnos a identificar el idioma que 
#se ha ingresado. Esto puede ser realmente útil si no estás seguro de qué idioma estás 
#tratando. 
#Puedes crear también una GUI sencilla para interactuar con el usuario. Después puedes 
#recopilar el texto del campo de entrada y procesarlo con "langdetect" para determinar qué 
#idioma se ingresó. Finalmente, puedes imprimir este resultado en la GUI para informar al 
#usuario sobre el resultado. 
#Ten en cuenta que los resultados devueltos por "langdetect" son códigos abreviados de 
#idioma. Por ejemplo, si ingresamos texto en inglés, veremos 'en' como el valor de retorno.

from tkinter import Tk, Label, Entry, Button, StringVar
from langdetect import detect


def detectar_idioma():
    texto = entrada.get()
    try:
        idioma = detect(texto)
        resultado.set(f"Idioma detectado: {idioma}")
    except Exception as e:
        resultado.set(f"Error: {str(e)}")


# Configurar ventana
ventana = Tk()
ventana.title("Detector de Idioma")
ventana.geometry("300x150")

# Elementos GUI
Label(ventana, text="Ingresa el texto:").pack(pady=5)
entrada = Entry(ventana, width=40)
entrada.pack(pady=5)

Button(ventana, text="Detectar Idioma", command=detectar_idioma).pack(pady=5)

resultado = StringVar()
Label(ventana, textvariable=resultado).pack(pady=5)

ventana.mainloop()
