# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def contador_letras(str):
    dfin = {}
    for i in str:
        if i in dfin:
            dfin[i] += 1
        else:
            dfin[i] = 1
    return (dfin)

def func_anagrama(pal1, pal2):
    return (contador_letras(pal1) == contador_letras(pal2))

print(func_anagrama("amorr","romar"))
print(func_anagrama("amor","pollo"))