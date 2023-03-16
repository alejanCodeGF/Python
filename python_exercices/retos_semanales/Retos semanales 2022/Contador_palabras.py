# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

def func_contador_palabras(str):
    dict_palabras = {} #key = palabra, valor = numero de veces que se repite
    signos_puntuacion = "[(¡¿,;:.-_!?)]"
    lista_palabras = str.split(' ')
    contador = 0
    for i in range(len(lista_palabras)): #para limpiar la palabra de signos de puntuación
        lista_palabras[i] = lista_palabras[i].lower()
        if lista_palabras[i][0] in signos_puntuacion:
            for x in lista_palabras[i]:
                if x not in signos_puntuacion:
                    break
                contador += 1
            lista_palabras[i] = lista_palabras[i][contador:]
            contador = 0
        if lista_palabras[i][-1] in signos_puntuacion:
            for x in lista_palabras[i][::-1]:
                if x not in signos_puntuacion:
                    break
                contador += 1
            lista_palabras[i] = lista_palabras[i][:-contador]
            contador = 0
    for i in range(len(lista_palabras)): #para meterla en el diccionario separada
        pass
        if lista_palabras[i] in dict_palabras:
            dict_palabras[lista_palabras[i]] += 1
        else:
            dict_palabras[lista_palabras[i]] = 1
    return dict_palabras

print(func_contador_palabras("Hola, mi nombre es .....brais. Mi nombre completo es Brais Moure (MoureDev))))))))))."))