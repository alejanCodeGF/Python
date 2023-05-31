# Creación de un sistema de gestión de inventarios: Para ordenar objetos, por ejemplo comida y tener organizado que cosas hay en casa

import typer

N_CAMPOS = 4 # Numero de objetos (2 botellas de agua p.e), cantidad del objeto(33 cl p.e), numero identificador (N1033 p.e, cada objeto con id),  descripción del objeto

def ver_inventario(l):
    for k,v in l.items():
        print(k, v)

def nuevo_objeto(l):
    print("¿Que objeto quieres añadir? ['exit']\n$ ", end="")
    while True:
        objeto = input()
        if (objeto == 'exit'):
            print('Ok pues deu')
            break
        if objeto in l.keys():
            print("Ya hay un objeto creado con ese nombre, cambia de nombre o ves al apartado de edición de objetos")
        else:
            i = 0
            l[objeto] = [0]*N_CAMPOS
            while i < N_CAMPOS:
                elemento = input(f"Introduzca la información del campo numero '{i+1}'\n$ ")
                l[objeto][i] = elemento
                i += 1
            print("Información introducida correctamente")
        print("¿Quieres añadir algun objeto más? ['exit']")

def eliminar_objeto(l):
    print("¿Que objeto quieres eliminar? ['exit']\n$ ", end="")
    while True:
        objeto = input()
        if (objeto == 'exit'):
            print('Ok pues deu')
            break
        elif objeto in l.keys():
            del l[objeto]
            print("Eliminado")
            print("¿Algun objeto más para eliminar? ['exit']\n$ ", end="")
        else:
            print("Por favor, introduce un objeto de la lista")
            print("¿Que objeto quieres eliminar? ['exit']\n$ ", end="")
    return

def editar_objeto(l):
    print("¿Que objeto quieres editar? ['exit']\n$ ", end="")
    while True:
        objeto = input()
        if (objeto == 'exit'):
            print('Ok pues deu')
            break
        elif objeto in l.keys():
            temp = l[objeto]
            if typer.confirm("¿Le quieres cambiar el nombre?"):
                del l[objeto]
                while True:
                    objeto = input("Introduce el nuevo nombre\n$ ")
                    if objeto not in l.keys():
                        break
                    print("Este nombre ya existe, utiliza otro nombre")
                l[objeto] = [0]*N_CAMPOS
            i = 0
            while i < N_CAMPOS:
                if typer.confirm(f"¿Le quieres cambiar la informacion del campo numero '{i+1}'?"):
                    elemento = input(f"Introduzca la información del campo\n$ ")
                    l[objeto][i] = elemento
                else:
                    l[objeto][i] = temp[i]
                i += 1
            return
        else:
            print("Por favor, introduce un objeto de la lista")
            print("¿Que objeto quieres editar? ['exit']\n$ ", end="")


def main():
    lista_objetos = {'a':[0,0,0,0], 'b':[0,0,0,0], 'c':[0,0,0,0], 'd':[0,0,0,0]} # Esto son ejemplos vaya
    while True:
        accion = input("¿Que deseas hacer? ['i'(ver inventario), 'n'(añadir objeto), 'd'(eliminar objeto), 'e'(editar objeto), 'exit']\n$ ")
        if (accion == 'i'):
            ver_inventario(lista_objetos)
        elif (accion == 'n'):
            nuevo_objeto(lista_objetos)
        elif (accion == 'd'):
            eliminar_objeto(lista_objetos)
        elif (accion == 'e'):
            editar_objeto(lista_objetos)
        elif (accion == 'exit'):
            print('Ok pues deu')
            break
        else:
            print("Por favor, introduce un comando posible")
            continue

if __name__ == "__main__":
    main()