import tkinter as tk
from tkinter import ttk

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
def calc(botones):
    global entrada
    calculadora = tk.Tk()
    calculadora.title('Calculadora Básica')
    calculadora.geometry('350x200')

    # Inicializa Filas y Columnas por si eventualmente se desea mover el conjunto
    i = 0 # Columnas
    j = 0 # Filas

    entrada = tk.Text(calculadora, height = 2, width = 30)
    entrada.grid(column = 1+i, row = 1+j, columnspan= 4)
    
    j += 1
    for bt in botones:
        boton = ttk.Button(text= bt['texto'], command= bt['funcion'])
        boton.grid(column= bt['col']+i, row= bt['fila']+j,columnspan= bt['tc'], rowspan= bt['tf'], )

    borrar()

    tk.mainloop()