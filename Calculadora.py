import os
import tkinter as tk
from tkinter import ttk

os.system('cls')
import botones

calculadora = tk.Tk()
calculadora.title('Básica')
calculadora.geometry('400x300')



botonesFn = [{'texto': '+', 'fg': 'black', 'funcion': 'sumar','col': 4, 'fila': 1, 'tf': 1, 'tc': 1},
         {'texto': '-', 'fg': 'black', 'funcion': 'restar','col': 4, 'fila': 2, 'tf': 1, 'tc': 1},
         {'texto': 'x', 'fg': 'black', 'funcion': 'multiplicar','col': 4, 'fila': 3, 'tf': 1, 'tc': 1},
         {'texto': '/', 'fg': 'black', 'funcion': 'dividir','col': 4, 'fila': 4, 'tf': 1, 'tc': 1},
         {'texto': '=', 'fg': 'black', 'funcion': 'igual','col': 3, 'fila': 4, 'tf': 1, 'tc': 1},
]



# Inicialización Filas y Columnas
i = 0
j = 0
for bt in botones.botonesNro:
    # print(bt['texto'])
    boton = ttk.Button(text= bt['texto'], command= bt['funcion'] )
    # boton.pack()
    boton.grid(column= bt['col']+i, row= bt['fila']+j,columnspan= bt['tc'], rowspan= bt['tf'])

for bt in botonesFn:
    # print(bt['texto'])
    boton = ttk.Button(text= bt['texto'])
    # boton.pack()
    boton.grid(column=bt['col']+i, row=bt['fila']+j)


tk.mainloop()