#La idea de este proyecto es crear un programa que pruebe la conectividad de sitios web. 
#Puedes usar los modulos urllib y tkinter para crear una interfaz gráfica de usuario (GUI) que 
#permita a los usuarios ingresar una dirección web. Después de haber recopilado la dirección 
#web del usuario, puedes pasarla a una función para devolver un código de estado HTTP para 
#el sitio web actual mediante la función .getcode() del módulo urllib. 
#En este ejemplo, simplemente determinamos si el código HTTP es 200. Si lo es, sabemos que 
#el sitio está funcionando; de lo contrario, informamos al usuario de que no está disponible.

#urllib para solicitud y error. tkinter para escribir mensaje.
import urllib.request
import urllib.error
import tkinter as tk
from tkinter import messagebox

def verificar_conectividad():
    url = entrada_url.get()
    if not url.startswith("http"):
        url = "http://" + url

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        respuesta = urllib.request.urlopen(req)
        codigo = respuesta.getcode()
        if codigo == 200:
            messagebox.showinfo("Resultado", f"El sitio web está disponible. (Código: {codigo})")
        else:
            messagebox.showwarning("Resultado", f"El sitio web no está disponible. (Código: {codigo})")
    except urllib.error.HTTPError as e:
        messagebox.showerror("Error HTTP", f"Código de error HTTP: {e.code}")
    except urllib.error.URLError as e:
        messagebox.showerror("Error de URL", f"Error de conexión: {e.reason}")

# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Verificador de Sitios Web")
ventana.geometry("400x150")

etiqueta = tk.Label(ventana, text="Introduce la URL del sitio web:")
etiqueta.pack(pady=10)

entrada_url = tk.Entry(ventana, width=50)
entrada_url.pack(pady=5)

boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_conectividad)
boton_verificar.pack(pady=10)

ventana.mainloop()
