import os
import tkinter as tk
from tkinter import ttk

os.system('cls')
import botones

calculadora = tk.Tk()
calculadora.title('Básica')
calculadora.geometry('400x300')

# Inicialización Filas y Columnas por si eventualmente se desea mover el conjunto
i = 0 # Columnas
j = 0 # Filas

entrada = tk.Text(calculadora, height = 1, width = 30)
entrada.grid(column = 1+i, row = 1+j, columnspan= 4)
j += 1

for bt in botones.botonesNro:
    boton = ttk.Button(text= bt['texto'], command= bt['funcion'] )
    boton.grid(column= bt['col']+i, row= bt['fila']+j,columnspan= bt['tc'], rowspan= bt['tf'])



tk.mainloop()