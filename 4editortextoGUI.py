#Crea una interfaz gráfica de usuario (GUI) para simular nuestro propio editor de texto. Este 
#ejemplo también utiliza componentes estándar de GUI, incluyendo etiquetas, botones y 
#campos de entrada. 
#Puedes añadir la capacidad de abrir y guardar archivos, al igual que un editor de texto real. 

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

# Defino funciones del programa (Abrir y Guardar)
def abrir_archivo():
    ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            texto.delete('1.0', tk.END)
            texto.insert(tk.END, archivo.read())

def guardar_archivo():
    ruta = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if ruta:
        with open(ruta, 'w', encoding='utf-8') as archivo:
            archivo.write(texto.get('1.0', tk.END))
        messagebox.showinfo("Guardado", "Archivo guardado correctamente")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Editor de Texto")
ventana.geometry("600x400")

# Crear botones
boton_abrir = tk.Button(ventana, text="Abrir", command=abrir_archivo)
boton_abrir.pack(pady=5)

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_archivo)
boton_guardar.pack(pady=5)

# Área de texto con scroll
texto = ScrolledText(ventana, wrap=tk.WORD)
texto.pack(expand=True, fill='both')

ventana.mainloop()
