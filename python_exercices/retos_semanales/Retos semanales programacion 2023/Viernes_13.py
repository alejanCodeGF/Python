# * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# * - La función recibirá el mes y el año y retornará verdadero o falso.

from datetime import datetime

def func_viernes_13(mes, año):
    input = datetime(year=año, month=mes, day=13)
    if input.isoweekday() == 5:
        return True
    return False

if func_viernes_13(3, 2021):
    print("Martes 13 detected")
else:
    print("Bienn todo controlado no hay")