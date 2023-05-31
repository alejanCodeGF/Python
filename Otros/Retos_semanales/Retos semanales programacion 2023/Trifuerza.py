#/*
# *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
# *
# * Crea un programa que dibuje una Trifuerza de "Zelda"
# * formada por asteriscos.
# * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
# * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
# *
# * Ejemplo: Trifuerza 2
# * 
# * ___*
# * __***
# * _*   *
# * *** ***
# *
# * _____*
# * ____***
# * ___*   *
# * __*** ***
# * _*   *   *
# * *** *** ***
# *
# */

# Procedimiento:
    # n = numero de triangulos, si por ejemplo sale 3 será (***_***_***) + (_*___*___*) + (__***_***) + (___*___*) + (____***) + (_____*)
    # Puedo hacer por filas, si es impar -> '*   ' x i (para que se redondé al numero de encima, le sumo 1), si es par -> '*** ' x i

def trifuerza(n):
    i = 1
    espacios = n*2 - 1
    while i <= n*2:
        if i%2 != 0: # Impar 
            print(espacios*' ' + (i+1)//2*'*   ')
        else:
            print(espacios*' ' + i//2*'*** ')
        espacios -= 1
        i += 1

def trifuerza_inversa(n):
    espacios = 0
    while n >= 0:
        print(espacios*' ' + n*'*** ')
        espacios += 1
        print(espacios*' ' + n*'*   ')
        espacios += 1
        n -= 1

n = 10
trifuerza(n)
trifuerza_inversa(n)