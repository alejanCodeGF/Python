#/*
# * Crea un programa que analice texto y obtenga:
# * - Número total de palabras.
# * - Longitud media de las palabras.
# * - Número de oraciones del texto (cada vez que aparecen un punto).
# * - Encuentre la palabra más larga.
# *
# * Todo esto utilizando un único bucle.
# */

# Procedimiento:
    # Numero total de palabras (n_pal), será cada vez que haya un espacio
    # Si hay espacio, contar la palabra, añadirla a la lista (l_pal) y saltar todos los espacios hasta la siguiente letra
    # Si hay un punto contar la palabra y sumar una oración y hacer lo mismo que los espacios
    # La palabra mas larga o con la lista, o hacer una variable que vaya cambiando a la palabra si es mas larga

def func_analisis_texto(texto):
    cond_palabra = 0
    cond_oracion = 0
    n_pal = 0
    l_pal = []
    longitud_pal = []
    n_ora = 0
    palabra = ''
    for letra in texto:
        if letra == ' ':
            if cond_palabra == 1:
                n_pal += 1
                cond_palabra = 0
                l_pal.append(palabra)
                longitud_pal.append(len(palabra))
                palabra = ''
        elif letra == '.':
            if cond_palabra == 1:
                n_pal += 1
                cond_palabra = 0
                l_pal.append(palabra)
                longitud_pal.append(len(palabra))
                palabra = ''
            if cond_oracion == 1:
                n_ora += 1
                cond_oracion = 0
        else:
            cond_palabra = 1
            cond_oracion = 1
            palabra += letra
    if letra != ' ' and letra != '.':
        l_pal.append(palabra)
        longitud_pal.append(len(palabra))
        n_pal += 1
    
    pal_larga = sorted(l_pal, key=len, reverse=True)[0]
    media = sum(longitud_pal) / len(l_pal)

    return n_pal, media, n_ora, pal_larga

def func_analisis_texto_V2(texto):
    palabras = texto.replace('.', ' ').split()
    n_pal = len(palabras)
    longitud_pal = [len(palabra) for palabra in palabras]
    n_ora = texto.count('.')
    pal_larga = max(palabras, key=len)
    media = sum(longitud_pal) / n_pal
    
    return n_pal, media, n_ora, pal_larga

texto = "Hola. que. tal. como. estas."
print(func_analisis_texto(texto))
print(func_analisis_texto_V2(texto))