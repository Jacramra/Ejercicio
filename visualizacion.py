# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Seaborn para visualizaciones más estilizadas
import seaborn as sns
import os
import tkinter as tk
from analisis import DataAnalyzer
from tkinter.scrolledtext import ScrolledText
from tkinter
from PIL import ImageTk

data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)
info = analizar.summary()

def informacion():
    try:
        text_area.delete("1.0",tk.END) #Para vaciar al ejecutar
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerror("Error", "No se puede")

def mostrar_imagenes(pil_img):
    image_tk = ImageTk.PhotoImage(pil_img)
    image_label.configure(image = image_tk)
    image_label.image = image_tk

ventana = tk.Tk()
ventana.title("Analisis de datos")

boton_summary = tk.Button(ventana, text="Resumen", command = informacion)
boton_summary.grid(row=0, column=0)

boton_summary = tk.Button(ventana, text="Númerico", command = informacion)
boton_summary.grid(row=0, column=1)

boton_summary = tk.Button(ventana, text="Categorico", command = informacion)
boton_summary.grid(row=0, column=2)


text_area = ScrolledText(ventana, width=70, height=30)
text_area.grid(row=1, column=1)

content_frame = tk.Frame(ventana)
content_frame = grid(row=1, column=2)
image_label = tk.label(content_frame, text="Resutado")
image_label.grid(row=0, column=0)
ventana.mainloop()

