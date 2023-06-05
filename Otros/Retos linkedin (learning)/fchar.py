# Devuelve el primer caracter que se repita (banana -> 'a')
# No puede ser el caracter "espacio"
# Si no lo encuentra devolver None
# fchar = first char, nose por poner algo

def fchar(texto):
    texto_fin = texto.lower()
    letras = []
    for i in texto_fin:
        if i == " ":
            pass
        elif i in letras:
            return i
        else:
            letras.append(i)
    return None


print(fchar("Hola mundo"))  # return o
print(fchar("Banana"))  # return a
print(fchar("Hola"))  # return None
print(fchar(""))  # return None
