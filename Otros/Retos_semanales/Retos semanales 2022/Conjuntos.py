# Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
# - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
# - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

def conjuntos(array1, array2, condicion):
    array_final = []
    set1 = set(array1)
    set2 = set(array2)
    if condicion:
        for i in set1:
            if i in set2:
                array_final.append(i)
    else:
        for i in set1:
            if i not in set2:
                array_final.append(i)
        for i in set2:
            if i not in set1:
                array_final.append(i)
    return tuple(array_final)

# Test:
print(conjuntos((1,2,3,4,5,6), (5,6,7,8,9,0), True))
print(conjuntos((1,2,3,4,5,6), (5,6,7,8,9,0), False))
