# Enunciado: Lee el fichero "Calculadora.txt" incluido en el proyecto, calcula su resultado e imprímelo.
# - El .txt se corresponde con las entradas de una calculadora.
# - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
# - Soporta números enteros y decimales.
# - Soporta las operaciones suma "+", resta "-", multiplicación "#" y división "/".
# - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
# - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.

# Mirar el txt y luego lo entenderás
# Error: 2 lineas seguidas de numeros, o de operaciones

def calculadora(archivo):
    nfin = 0
    numero = 0 # Numero que guardas, y luego lo multiplicas por el siguiente
    num_op = 0 # 0 si es una operación y 1 si es un numero (mira el anterior vaya)
    file = open(archivo, "r")
    lista_fichero = file.readlines()
    for i in lista_fichero:
        i.replace('\n', '')
        if num_op == 0 and i.isnumeric():
            nfin = 
        if num_op == 1 and i in "+-#/":
            if i == "+":
                # Esto es una chusta
    file.close()
    return
# Plan:
    # Recorrer linea a linea y ponerlo todo en una variable ntotal, tener en cuenta cuando es numero, para que no hayan 2 lineas de numeros seguidas (y lo mismo con operaciones)

# Test:
calculadora("Calculadora.txt")