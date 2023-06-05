# Dada una lista de numeros, ordenarlos con la ordenación de la burbuja (ordena por capas, con 2 whiles)
# Soy un mago, me ha salido a la primera
# Lo que hago es comparo el lista[i] con el lista[j]. Al principio son i=0, j=1 luego i=0, j=2 hasta que encuentre que el numero es mas pequeño
# Si lo es, hace un break y vuelve a hacer lo mismo (osea hasta que en la primera posición esté el numero mas pequeño), y luego con i = 1, i = 2... hasta acabarlo
# Un else despues de un while hace que SOLO CUANDO SE CUMPLA EL WHILE (osea no hace break) lo hará. Si no pasa la linea

def ordenar_lista(lista):
    aux = 0
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                break
            j += 1
        else:
            i += 1
    return (lista)


print(ordenar_lista([1, 4, 0, 1, 2, 0, 1, 2,
      2, 4, 6, 7, 8, 8, 1, 12, 3, 1, 1, 2, 1]))
