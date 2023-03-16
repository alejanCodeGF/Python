# Hcer un programa de adivinar el codigo de colores, si tienes el color en la posicion correcta o si tienes un color que esta en el codigo, te avisa
# 4 conceptos:
    # Crear un codigo
    # Que el usuario meta un codigo correcto
    # Comparar el codigo
    # Ajuntar todo

import random

COLORS = ["R", "G", "B", "Y", "W", "O"] #Red, Green, Blue, Yellow, White, Orange
TRIES = 12
CODE_LENGTH = 5

# Generador de codigo
def code_generator():
    code = []
    for _ in range(CODE_LENGTH): # (el "_" es simplemente para hacer una variable anonima, que no voy a usar)
        code.append(random.choice(COLORS))
    return code

# Interaccion del usuario
def guess_code():

    while True: # Para repetir el proceso hasta que el jugador de una respuesta correcta
        guess = input("Guess: ").upper().split(" ") # input == "G G G G" (y si hay una minuscula, la haga mayuscula) -> ["G","G","G","G"]
        if len(guess) != CODE_LENGTH:
            print(f"Numero de colores incorrecto, tienen que ser {CODE_LENGTH} numeros.")
            continue # Me vuelve al pincipio del loop

        for color in guess:
            if color not in COLORS:
                print(f"Color introducido '{color}' no correcto, por favor escriba uno de estos colores:", *COLORS)
                break
        else:
            break

    return guess

def compare_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Creo un diccionario para tener en cuenta cuantos colores hay
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
    
    for guess_color, real_color in zip(guess, real_code): # Zip == "creador de parejas" --> [...,(guess[i], real_code[i]), (guess[i+1], real_code[i+1]),...]
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1
    
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in real_code and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

# Aqui ira estructurado todas las funciones
def game():
    print(f"Los colores que puedes usar son:", *COLORS)
    code = code_generator()
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = compare_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"¡Enhorabuena! Has encontrado el codigo en {attempts} intentos")
            break

        print(f"Posición correcta: {correct_pos} | Posición incorrecta: {incorrect_pos}")

    else:
        print(f"Te quedaste sin intentos makena, el codigo correcto era ", *code)

if __name__ == "__main__": # Se ejecuta solo cuando el archivo en el que se encuentra es ejecutado directamente como programa, si importamos el fichero a otro programa no lo hará (solo pillará las funciones)
    print(f"Bienvenido a Mastermind, tienes {TRIES} intentos hasta encontrar el codigo correcto")
    while 1:
        game()
        respuesta = input("¿Quieres jugar otra partida? (y/n)\n$ ")
        if respuesta.upper() == "Y":
            continue
        if respuesta.upper() == "N":
            break
        else:
            print("que dise tonto polla, pues que te den te saco del bucle")
            break
