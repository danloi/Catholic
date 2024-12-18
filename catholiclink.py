import tkinter as tk
import webbrowser

def abrir_magisterium():
    webbrowser.open('https://www.magisterium.com/es')

def abrir_categpt():
    webbrowser.open('https://categpt.chat')
def abrir_catholic():
    webbrowser.open('https://www.catholic.chat')
    

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lanzador de ChatBots")
ventana.geometry("300x300")

# Crear etiqueta de título
etiqueta = tk.Label(ventana, text="Elige un ChatBot", font=("Arial", 14))
etiqueta.pack(pady=20)

# Crear botones
boton_catholic = tk.Button(ventana, text="Católico", command=abrir_catholic, width=15, height=2)
boton_catholic.pack(pady=10)

boton_magisterium = tk.Button(ventana, text="Magisterium", command=abrir_magisterium, width=15, height=2)
boton_magisterium.pack(pady=10)

boton_categpt = tk.Button(ventana, text="CateGPT", command=abrir_categpt, width=15, height=2)
boton_categpt.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()

