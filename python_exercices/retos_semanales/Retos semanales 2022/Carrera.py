# Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
# carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras "run" o "jump"
#      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#        variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
# - Si hace "run" en "|" (valla), se variará la pista por "/".
# - La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

# Entiendo que tiene que hacerlo perfecto para completar la carrera.
# Tiene que haber una variable que reescriba la pista, si lo hace correcto lo dejas igual si no "x" o "/" depende de como lo haga mal
# Entiendo también que el numero de acciones es igual al numero de obstaculos de la pista (igualmente acoto errores)

def func_errores(array_acciones, str_pista):
    if set(str_pista) != set("|_"): # Comprobar luego esta shet de casos que no van cuando funcione
        print("error, no has escrito bien la pista de obstaculos")
    elif set(array_acciones) != set(["run", "jump"]):
        print("error, no has escrito bien las acciones")
    elif len(str_pista) != len(array_acciones):
        print("error, el numero de acciones no es igual a la longitud de la pista")
    else:
        return 0
    return 1

def carrera_obstaculos(array_acciones, str_pista):
    str_pista_recorrida = ""
    if func_errores(array_acciones, str_pista):
        return
    for i, accion in enumerate(array_acciones):
        if str_pista[i] == "_":
            if accion == "run":
                str_pista_recorrida += str_pista[i]
            else:
                str_pista_recorrida += "x"
        elif str_pista[i] == "|":
            if accion == "jump":
                str_pista_recorrida += str_pista[i]
            else:
                str_pista_recorrida += "/"
    return not ("/" in str_pista_recorrida or "x" in str_pista_recorrida)

# Plan:
    # for i,accion in enumerate(array_acciones):
        # Posicion i es la del str y accion es la accion que hace
        # Si es correr: 
            #si es correcto, bien, si no lo es, mal
        # Si es salto:
            #si es correcto, bien, si no lo es, mal
    # Comprueba si ha habido algun error


# Test:
print(carrera_obstaculos(("run", "run", "jump", "run", "jump", "run", "run", "jump", "jump", "run", "jump"),"__|_|__||_|")) # Este es completamente correcto

# Otra forma de verlo
# El numero de acciones y de la pista pueden ser diferentes
# Continuar el proceso hasta que complete o las acciones o la pista (p.e se puede equivocar las veces que quiera, mientras al final complete la pista correctamente)
# Tiene que haber una variable que reescriba la pista, si lo hace correcto lo dejas igual si no "x" o "/" depende de como lo haga mal

def func_errores_V2(array_acciones, str_pista):
    if set(str_pista) != set("|_"): # Comprobar luego esta shet de casos que no van cuando funcione
        print("error, no has escrito bien la pista de obstaculos")
    elif set(array_acciones) != set(["run", "jump"]):
        print("error, no has escrito bien las acciones")
    else:
        return 0
    return 1

def carrera_obstaculos_V2(array_acciones, str_pista):
    str_pista_recorrida = ""
    if func_errores_V2(array_acciones, str_pista):
        return
    i = 0 # CONTADOR DE LA POSICION DE LA PISTA EN LA QUE ESTAMOS
    for accion in array_acciones:
        if str_pista[i] == "_":
            if accion == "run":
                str_pista_recorrida += str_pista[i]
                i += 1
            else:
                str_pista_recorrida += "x"
        elif str_pista[i] == "|":
            if accion == "jump":
                str_pista_recorrida += str_pista[i]
                i += 1
            else:
                str_pista_recorrida += "/"
        if i == len(str_pista): # Si completa el circuito antes de acabar las acciones, return True
            #print(str_pista_recorrida)
            return True
    #print(str_pista_recorrida)
    return False # Si ha acabado las acciones y no lo ha completado, return False

# Plan:
    # Hacemos otra vez for con las array acciones
        # Si completa la pista sale del bucle y return true
        # Si no lo completa cuando acabe el bucle return false
    # Para saber si ha completado la pista, el len(pista) == i(posicion en la que estamos de la pista (solo suma si es correcto))


# Test:
print(carrera_obstaculos_V2(("run", "run", "jump", "run", "jump", "run", "run", "jump", "jump", "run", "jump"),"__|_|__||_|")) # Este es completamente correcto
print(carrera_obstaculos_V2(("run", "run", "run", "jump", "run", "jump", "run", "jump", "jump", "jump", "jump", "jump",  "run", "jump"), "_|_|__|_|"))