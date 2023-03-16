# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.

import unicodedata

def func_palindromo(pal1):
    pal1fin = ""
    excepciones = " ¡!¿?.,;:«»“”‘’'—-()[]{}@#$%&"
    tildes = {"Á":"a","À":"a","Ä":"a","á":"a","à":"a","ä":"a","É":"e","È":"e","Ë":"e","é":"e","è":"e","ë":"e","Í":"i","Ì":"i",
    "Ï":"i","í":"i","ì":"i","ï":"i","Ó":"o","Ò":"o","Ö":"o","ó":"o","ò":"o","ö":"o","Ú":"u","Ù":"u","Ü":"u","ú":"u","ù":"u","ü":"u"}
    for i in pal1:
        if i in tildes:
            pal1fin += tildes[i]
        elif i not in excepciones:
            pal1fin += i
    pal1fin = pal1fin.lower()
    return pal1fin == pal1fin[::-1]

print(func_palindromo("Aná llevá al osó-!? la avellaná"))
print(func_palindromo("popopopopopopopopopopopop"))