# anagrama = palabra que tiene la mismas letras que otra, tanto letras como numero de letras
# return true si lo son return false si no
# Da igual las mayusculas de la palabra


def n_letras(texto):
    d = dict()
    for i in texto:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def is_anagrama(palabra1, palabra2):
    letras1 = n_letras(palabra1)
    letras2 = n_letras(palabra2)
    if letras1 == letras2:
        return True
    return False


print(is_anagrama("ramo", "mora"))  # True
print(is_anagrama("ramos", "moras"))  # True
print(is_anagrama("ramo", "moro"))  # False
