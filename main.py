

from Calculadora import colocarNumero, operacion, borrar, calc


botones = [{'texto': '0', 'funcion': lambda: colocarNumero(0),'col': 2, 'fila': 4, 'tf': 1, 'tc': 1},
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

calc(botones)