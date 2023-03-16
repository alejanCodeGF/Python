# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str

def func_unique_char(str):
    l = []
    for i in str:
        if i not in l:
            l.append(i)
    return (l)
#    return list(set(str)) otra forma de hacerlo (Lo hace set, para quitar repetidos, luego lo hace lista)

def func_car_nocomunes(str1, str2):
    out1 = out2 = ""
    lstr1 = func_unique_char(str1)
    lstr2 = func_unique_char(str2)
    for i in str1:
        if i not in lstr2:
            out1 += i
    for i in str2:
        if i not in lstr1:
            out2 += i
    return (out1, out2)

print(func_car_nocomunes("abcdef","defghi"), func_car_nocomunes("brais","moure"), func_car_nocomunes("Me gusta Java","Me gusta Kotlin"), end = " ")
print(func_car_nocomunes("Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad", 
"Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada."))