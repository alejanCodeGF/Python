 # Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 # Podrás configurar generar contraseñas con los siguientes parámetros:
 # - Longitud: Entre 8 y 16.
 # - Con o sin letras mayúsculas.
 # - Con o sin números.
 # - Con o sin símbolos.
 # (Pudiendo combinar todos estos parámetros entre ellos)

import random

def func_pass_generator():
    password = ""
    listacar = list(map(chr, range(33, 127))) #Desde '¡' hasta '~', pasando por letras, numeros y simbolos
    lon = random.randrange(8, 17)
    for i in range(lon):
        password += listacar[random.randrange(0, len(listacar))]
    return password
    
print("Contraseña de la forma 1:", func_pass_generator())
#mequivocao xd no se referia a esto

def password_generator(length=8, capital=False, numbers=False, symbols=False):
    password = ""
    if length < 8 or length > 16:
        print("Contraseña demasiado corta o demasiado larga, introduzca una longitud entre 8 y 16")
        return password
    listacar = list(map(chr, range(97, 123)))
    if capital:
        listacar += list(map(chr, range(65, 91)))
    if numbers:
        listacar += list(map(chr, range(48, 58)))
    if symbols:
        listacar += list(map(chr, range(33, 48))) + list(map(chr, range(58, 65))) 
        listacar += list(map(chr, range(91, 97))) + list(map(chr, range(123, 127)))
    for i in range(length):
        password += listacar[random.randrange(0, len(listacar))]
    return password

print("Contraseña de la forma 2:", password_generator(10,1,1,1))