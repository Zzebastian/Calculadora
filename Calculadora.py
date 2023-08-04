import os
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
try:
    os.system('clear')
except:
    os.system('cls')

def borrar():
    global primerNumero, segundoNumero, evitarSuperposicion, tareaprevia
    primerNumero = None
    segundoNumero = None
    evitarSuperposicion = False
    tareaprevia = ''
    entrada.delete('1.0', 'end')
#

def colocarNumero(numero):
    global evitarSuperposicion
    
    if evitarSuperposicion != False:
        entrada.delete('1.0', 'end')
        evitarSuperposicion = False
    
    entrada.insert(tk.END, numero)
# 
def operacion(tarea):
    global primerNumero, segundoNumero, evitarSuperposicion, tareaprevia
    
    if tareaprevia != '':
        segundoNumero = int(entrada.get('1.0', 'end'))
        accion(tareaprevia)
        tareaprevia = tarea

        if tarea == 'igual':
            tareaprevia = ''
            primerNumero = None
            segundoNumero = None

    elif primerNumero == None:
        try:
            primerNumero = int(entrada.get('1.0', 'end'))
        except:
            primerNumero = 0
        
        tareaprevia = tarea
    else:
        segundoNumero = int(entrada.get('1.0', 'end'))

    
    evitarSuperposicion = True   
#
def accion(tareaprevia):
    global primerNumero, segundoNumero

    if tareaprevia == 'sumar':
        primerNumero += segundoNumero
    elif tareaprevia == 'restar':
        primerNumero -= segundoNumero
    elif tareaprevia == 'multiplicar':
        primerNumero *= segundoNumero
    elif tareaprevia == 'dividir':
        primerNumero /= segundoNumero
    
    entrada.delete('1.0', 'end')
    entrada.insert(tk.END, primerNumero)

#

botonesNro = [{'texto': '0', 'funcion': lambda: colocarNumero(0),'col': 2, 'fila': 4, 'tf': 1, 'tc': 1},
        {'texto': '1', 'funcion': lambda: colocarNumero(1),'col': 1, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '2', 'funcion': lambda: colocarNumero(2),'col': 2, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '3', 'funcion': lambda: colocarNumero(3),'col': 3, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '4', 'funcion': lambda: colocarNumero(4),'col': 1, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': '5', 'funcion': lambda: colocarNumero(5),'col': 2, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': '6', 'funcion': lambda: colocarNumero(6),'col': 3, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': '7', 'funcion': lambda: colocarNumero(7),'col': 1, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '8', 'funcion': lambda: colocarNumero(8),'col': 2, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '9', 'funcion': lambda: colocarNumero(9),'col': 3, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '+', 'funcion': lambda: operacion('sumar'),'col': 4, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '-', 'funcion': lambda: operacion('restar'),'col': 4, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': 'x', 'funcion': lambda: operacion('multiplicar'),'col': 4, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '/', 'funcion': lambda: operacion('dividir'),'col': 4, 'fila': 4, 'tf': 1, 'tc': 1},
        {'texto': '=', 'funcion': lambda: operacion('igual'),'col': 3, 'fila': 4, 'tf': 1, 'tc': 1},
        {'texto': 'C', 'funcion': lambda: borrar(),'col': 1, 'fila': 4, 'tf': 1, 'tc': 1},
]


calculadora = tk.Tk()
calculadora.title('Calculadora Básica')
calculadora.geometry('350x200')

# Inicializa Filas y Columnas por si eventualmente se desea mover el conjunto
i = 0 # Columnas
j = 0 # Filas


entrada = tk.Text(calculadora, height = 2, width = 30)
entrada.grid(column = 1+i, row = 1+j, columnspan= 4)
j += 1

for bt in botonesNro:
    boton = ttk.Button(text= bt['texto'], command= bt['funcion'])
    boton.grid(column= bt['col']+i, row= bt['fila']+j,columnspan= bt['tc'], rowspan= bt['tf'], )

borrar()

tk.mainloop()