# * Crea 3 funciones, cada una encargada de detectar si una cadena de
# * texto es un heterograma, un isograma o un pangrama.
# * - Debes buscar la definición de cada uno de estos términos.

# Heterograma: No se repite ninguna letra
# Isograma: Cada letra aparece el mismo numero de veces (si solo se repiten 1 vez será heterograma y isograma)
# Pangrama: Que contiene todas las letras del abecedario

# Lo haré con diccionarios, para sacar el numero de veces que se repite cada letra, y luego paso el filtro para que detecte el tipo de palabra

import string

def num_letras(str):
    dic = {}
    for char in str:
        char = char.lower()
        if char not in string.ascii_lowercase and char != "ñ":
            pass
        elif char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic

def hetero_iso_pana(str):
    resultado = []
    letras = num_letras(str)
    condicion = 0 # Si condición es 0, no es ni hetero ni iso, si es 1 depende del numero de letras de cada uno
    i = 0 # Si es igual al numero de letras del abecedario, será pangrama
    n = list(letras.values())[0]
    for letra in letras.values():
        i += 1
        if n != letra:
            condicion = 1
    if condicion == 0:
        if n == 1:
            resultado.append("Heterograma")
            resultado.append("Isograma")
        else:
            resultado.append("Isograma")
        if i == 27:
                resultado.append("Pangrama")
    else:
        if i == 27:
                resultado.append("Pangrama")
    return resultado
        

# Heterogramas: yuxtaponer (10), centrifugado (12), luteranismo (11), adulterinos (11), hiperblanduzcos (15)...
# Isogramas con una o dos repeticiones: acondicionar (11), escritura (9), intestinos (10), papelera (8)...
# Pangrama: Benjamín pidió una bebida de kiwi y fresa.

print(hetero_iso_pana("yuxtaponer"))
print(hetero_iso_pana("centrifugado"))
print(hetero_iso_pana("El veloz murcielago hindu comia feliz cardillo y kiwi. La cigueña tocaba el saxofon detras del palenque de paja"))
print(hetero_iso_pana("Jovencillo emponzoñado de whisky, ¡que figurota exhibe!"))