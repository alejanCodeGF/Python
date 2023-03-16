# Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

from datetime import date

def diferencia_dias_txt(str1, str2):
    if False: # xx/xx/xxxx mirarlo con expresiones regulares (en teoria seria "^\d{2}/\d{2}/\d{4}$" igual habria que poner algo para las / que separan cada numero)
        print("Ha habido un error, compruebe todo por favor")
        return
    else:
        n1 = [int(str1[0])*10 + int(str1[1]), int(str1[3])*10 + int(str1[4]), int(str1[6])*1000 + int(str1[7])*100 + int(str1[8])*10 + int(str1[9])]
        n2 = [int(str2[0])*10 + int(str2[1]), int(str2[3])*10 + int(str2[4]), int(str2[6])*1000 + int(str2[7])*100 + int(str2[8])*10 + int(str2[9])]
        d1 = date(day = n1[0], month = n1[1], year = n1[2])
        d2 = date(day = n2[0], month = n2[1], year = n2[2])
        return abs(d1 - d2)

print(diferencia_dias_txt("05/09/1900","06/09/2001"))