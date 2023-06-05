# Son las listas sin otras listas dentro de ellas
# Dada una lista de 2 dimensiones (1 dentro de otra) dará otra lista de una dimension con todos los elementos ([1,2,3,[1,2]] == [1,2,3,1,2])

def flatten_a_list(lista):
    flattened_list = []
    for elemento in lista:
        if type(elemento) == list:
            for elemento2 in elemento:
                flattened_list.append(elemento2)
        else:
            flattened_list.append(elemento)
    return flattened_list


print(flatten_a_list([1, 2, 3, [1, 2]]))
