# Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.

def func_conversor(d, h, m, s):
    h += d*24
    m += h*60
    s += m*60
    return s*1000

print(func_conversor(0, 0, 0, 10))
print(func_conversor(2, 5, -45, 10))
print(func_conversor(2000000000, 5, 45, 10))