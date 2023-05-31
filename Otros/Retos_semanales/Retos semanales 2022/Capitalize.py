# Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
# poner en mayúscula la primera letra de cada palabra.
# - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

# Entiendo que una palabra es un conjunto de caracteres alphanumericos, separados por los demás caracteres (43juan -> 43juan, paco43pinga -> Paco43pinga)

def func_capitalize(str):
    str_fin = ""
    sum_char = 0
    pal = 0
    for character in str:
        if character == ' ': # No quiero que los espacios los tome como caracteres, y de esta forma pasan de largo
            pal = 0
        elif pal == 0 and character.isalnum():
            str_fin += character.upper()
            character = '' # Para que al final str_fin += char no repita letra (lo tengo asi porque se simplifica mucho)
            pal = 1
        elif pal == 1 and not character.isalnum():
            pal = 0
        str_fin += character
    print(str_fin)

# Plan a seguir:
    # Str vacio de return
    # Usar una variable pal = 0 si no está en una palabra, pal = 1 si esta en la palabra
    # Cuando esté empezando una palabra, hace mayuscula, pal = 1... cuando acabe la palabra pal = 0, y hasta el infinito

# tests:
func_capitalize("que dise el tio, como te encuentras hoy loketex? Jajaj lol")
func_capitalize("43juan/paco Erlado")