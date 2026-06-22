print("Hola mundo desde GIT")
import tkinter as tk

root = tk.Tk()
root.title("Mi primera app con Tkinter")

# Establece el tamaño de la ventana: 400 píxeles de ancho y 200 de alto
root.geometry("400x200")

label = tk.Label(root, text="¡Hola mundo!", font=("Arial", 18))
label.pack(pady=50)  # Padding vertical para centrar mejor el texto

root.mainloop()

import tk
root = tk.Root()
root.do_something()