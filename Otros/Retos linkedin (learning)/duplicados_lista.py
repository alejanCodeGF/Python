# Devuelve lista de solo los elementos que se repiten

def encontrar_duplicados_lista(lista):
    l2 = []
    lfin = []
    for i in lista:
        if i not in l2:
            l2.append(i)
        else:
            lfin.append(i)
    return lfin


print(encontrar_duplicados_lista(
    [0, 0, 0, 0, 0, 0, 10, 1, 1, 1, 0, 1, 2, 2, 3, 4, 5]))
