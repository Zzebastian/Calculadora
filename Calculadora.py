import os
import tkinter as tk
from tkinter import ttk

os.system('cls')

primerNumero = None
segundoNumero = None
evitarSuperposicion = False

def colocarNumero(numero):
    global evitarSuperposicion
    if evitarSuperposicion != False:
        entrada.delete('1.0', 'end')
        evitarSuperposicion = False
    
    entrada.insert(tk.END, numero)
# 
def operacion(tarea):
    global primerNumero, segundoNumero, evitarSuperposicion
    if primerNumero == None:
        primerNumero = int(entrada.get('1.0', 'end'))

    else:
        segundoNumero = int(entrada.get('1.0', 'end'))
        accion(tarea)
        entrada.delete('1.0', 'end')
        entrada.insert(tk.END, primerNumero)
        print(segundoNumero)
        segundoNumero = None

    evitarSuperposicion = True
    print(primerNumero)
# 
def accion(tarea):
    global primerNumero, segundoNumero

    if tarea == 'sumar':
        primerNumero += segundoNumero
    elif tarea == 'restar':
        primerNumero -= segundoNumero
    elif tarea == 'multiplicar':
        primerNumero *= segundoNumero
    elif tarea == 'dividir':
        primerNumero /= segundoNumero
    
#
def igual():
    print('igual')
# 


botonesNro = [{'texto': '0', 'fg': 'black', 'funcion': lambda: colocarNumero(0),'col': 1, 'fila': 4, 'tf': 1, 'tc': 2},
        {'texto': '1', 'fg': 'black', 'funcion': lambda: colocarNumero(1),'col': 1, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '2', 'fg': 'black', 'funcion': lambda: colocarNumero(2),'col': 2, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '3', 'fg': 'black', 'funcion': lambda: colocarNumero(3),'col': 3, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '4', 'fg': 'black', 'funcion': lambda: colocarNumero(4),'col': 1, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': '5', 'fg': 'black', 'funcion': lambda: colocarNumero(5),'col': 2, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': '6', 'fg': 'black', 'funcion': lambda: colocarNumero(6),'col': 3, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': '7', 'fg': 'black', 'funcion': lambda: colocarNumero(7),'col': 1, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '8', 'fg': 'black', 'funcion': lambda: colocarNumero(8),'col': 2, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '9', 'fg': 'black', 'funcion': lambda: colocarNumero(9),'col': 3, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '+', 'fg': 'black', 'funcion': lambda: operacion('sumar'),'col': 4, 'fila': 1, 'tf': 1, 'tc': 1},
        {'texto': '-', 'fg': 'black', 'funcion': lambda: operacion('restar'),'col': 4, 'fila': 2, 'tf': 1, 'tc': 1},
        {'texto': 'x', 'fg': 'black', 'funcion': lambda: operacion('multiplicar'),'col': 4, 'fila': 3, 'tf': 1, 'tc': 1},
        {'texto': '/', 'fg': 'black', 'funcion': lambda: operacion('dividir'),'col': 4, 'fila': 4, 'tf': 1, 'tc': 1},
        {'texto': '=', 'fg': 'black', 'funcion': lambda: operacion('igual'),'col': 3, 'fila': 4, 'tf': 1, 'tc': 1},
]





calculadora = tk.Tk()
calculadora.title('Básica')
calculadora.geometry('400x300')

# Inicialización Filas y Columnas por si eventualmente se desea mover el conjunto
i = 0 # Columnas
j = 0 # Filas

entrada = tk.Text(calculadora, height = 1, width = 30)
entrada.grid(column = 1+i, row = 1+j, columnspan= 4)
j += 1

for bt in botonesNro:
    boton = ttk.Button(text= bt['texto'], command= bt['funcion'] )
    boton.grid(column= bt['col']+i, row= bt['fila']+j,columnspan= bt['tc'], rowspan= bt['tf'])



tk.mainloop()