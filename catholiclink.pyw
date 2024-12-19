# Librerías a importar 

import tkinter as tk
from tkinter import ttk
import webbrowser
import time
import platform
import os

try:
    import psutil
except ImportError:
    import subprocess
    import sys
    import psutil

def get_sistema_info():
    sistema = platform.system()
    if sistema == "Linux":
        try:
            distro = platform.linux_distribution()[0]
        except:
            try:
                import distro
                distro = distro.name()
            except:
                distro = "Distribución desconocida"
        sistema = f"Linux ({distro})"
    
    procesador = platform.processor() or platform.machine()
    ram_total = round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2)
    
    return {
        'sistema': sistema,
        'procesador': procesador,
        'ram': f"{ram_total} GB"
    }

def abrir_email():
    webbrowser.open('mailto:losada.ehu@gmail.com')

def mostrar_about():
    # Crear ventana About
    about_window = tk.Toplevel()
    about_window.title("Acerca de")
    about_window.geometry("300x200")
    
    # Centrar la ventana
    x = about_window.winfo_screenwidth() // 2 - 150
    y = about_window.winfo_screenheight() // 2 - 100
    about_window.geometry(f"300x200+{x}+{y}")
    
    # Contenido de la ventana About
    tk.Label(about_window, text="Catholic Launcher", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(about_window, text="Versión 1.0", font=("Arial", 10)).pack()
    tk.Label(about_window, text="© 2024 Catholic Software", font=("Arial", 10)).pack()
    tk.Label(about_window, text="\nDesarrollado por:", font=("Arial", 10)).pack()
    tk.Label(about_window, text="Daniel Losada", font=("Arial", 10, "bold")).pack()
    
    # Email como enlace
    email_link = tk.Label(about_window, text="contacto@ejemplo.com", 
                         font=("Arial", 10), 
                         fg="blue", 
                         cursor="hand2")
    email_link.pack()
    email_link.bind("<Button-1>", lambda e: abrir_email())
    
    # Botón para cerrar
    tk.Button(about_window, text="Cerrar", command=about_window.destroy).pack(pady=20)

def actualizar_barra(barra_progreso, ventana_splash):
    for i in range(101):
        barra_progreso['value'] = i
        ventana_splash.update()
        time.sleep(0.02)
    ventana_splash.destroy()
    mostrar_ventana_principal()

def mostrar_ventana_principal():
    def abrir_magisterium():
        webbrowser.open('https://www.magisterium.com/es')

    def abrir_categpt():
        webbrowser.open('https://categpt.chat')

    def abrir_catholic():
        webbrowser.open('https://www.catholic.chat')

    # Obtener información del sistema
    info_sistema = get_sistema_info()

    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Lanzador de ChatBots")
    ventana.geometry("400x450")  # Aumentado para el nuevo botón

    # Usar os.path para la ruta del icono
    icon_path = os.path.join('images', 'cruz.ico')
    try:
        ventana.iconbitmap(icon_path)
    except:
        print(f"No se pudo cargar el icono desde: {icon_path}")

    # Frame para la información del sistema
    frame_info = tk.Frame(ventana, relief=tk.GROOVE, borderwidth=2)
    frame_info.pack(fill=tk.X, padx=10, pady=10)

    # Etiquetas con la información del sistema
    tk.Label(frame_info, text=f"Sistema: {info_sistema['sistema']}", anchor="w").pack(fill=tk.X, padx=5, pady=2)
    tk.Label(frame_info, text=f"Procesador: {info_sistema['procesador']}", anchor="w").pack(fill=tk.X, padx=5, pady=2)
    tk.Label(frame_info, text=f"Memoria RAM: {info_sistema['ram']}", anchor="w").pack(fill=tk.X, padx=5, pady=2)

    # Separador
    ttk.Separator(ventana, orient='horizontal').pack(fill='x', padx=10, pady=5)

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

    # Separador antes del botón About
    ttk.Separator(ventana, orient='horizontal').pack(fill='x', padx=10, pady=5)

    # Botón About
    boton_about = tk.Button(ventana, text="About", command=mostrar_about, width=15)
    boton_about.pack(pady=10)

    ventana.mainloop()

# Crear ventana de splash
ventana_splash = tk.Tk()
ventana_splash.title("Cargando")
ventana_splash.geometry("300x150")

# Centrar la ventana de splash
ancho_ventana = 300
alto_ventana = 150
x_ventana = ventana_splash.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana_splash.winfo_screenheight() // 2 - alto_ventana // 2
ventana_splash.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

# Etiqueta de carga
etiqueta_carga = tk.Label(ventana_splash, text="Cargando...", font=("Arial", 12))
etiqueta_carga.pack(pady=20)

# Barra de progreso
barra_progreso = ttk.Progressbar(ventana_splash, length=200, mode='determinate')
barra_progreso.pack(pady=20)

# Iniciar la actualización de la barra
ventana_splash.after(100, lambda: actualizar_barra(barra_progreso, ventana_splash))

ventana_splash.mainloop()