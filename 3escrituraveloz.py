#La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una 
#oración de manera precisa. 
#Este programa puede requerir crear una interfaz gráfica de usuario (GUI) mediante el módulo 
#tkinter. Si eres nuevo en las GUI, este ejemplo es una buena introducción, ya que tan solo 
#necesitas crear una serie de etiquetas simples, botones y campos de entrada para crear una 
#ventana. Puedes usar el módulo timeit de Python para manejar el aspecto de temporización 
#de nuestra prueba de escritura, y el módulo random para seleccionar aleatoriamente una frase 
#de prueba.

import tkinter as tk
import timeit
import random

phrases = [
    "La velocidad es esencial en la programación.",
    "Python es un lenguaje de alto nivel.",
    "Escribir código limpio es una buena práctica.",
    "La depuración es parte del desarrollo.",
    "Automatiza todo lo que puedas."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Prueba de velocidad de escritura")

        self.phrase = random.choice(phrases)

        self.label = tk.Label(root, text=f"Escribe esta frase:", font=("Arial", 12))
        self.label.pack(pady=(10, 0))

        self.phrase_label = tk.Label(root, text=self.phrase, wraplength=400, font=("Arial", 14), fg="blue")
        self.phrase_label.pack(pady=5)

        self.entry = tk.Entry(root, width=60, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)

        self.button = tk.Button(root, text="Evaluar", command=self.evaluate)
        self.button.pack(pady=10)

        self.result = tk.Label(root, text="", font=("Arial", 12))
        self.result.pack(pady=10)

        self.start_time = None

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = timeit.default_timer()

    def evaluate(self):
        end_time = timeit.default_timer()
        time_taken = end_time - self.start_time if self.start_time else 0

        typed_text = self.entry.get()
        if typed_text.strip().lower() == self.phrase.strip().lower():
            self.result.config(text=f"¡Correcto! Tiempo: {time_taken:.2f} segundos")
        else:
            self.result.config(text="Texto incorrecto. Intenta de nuevo.")

if __name__ == '__main__':
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
    