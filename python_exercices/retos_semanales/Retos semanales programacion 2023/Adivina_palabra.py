# * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
# * - El juego comienza proponiendo una palabra aleatoria incompleta
# *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
# * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
# *   la palabra a adivinar)
# *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
# *     uno al número de intentos
# *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
# *     al número de intentos
# *   - Si el contador de intentos llega a 0, el jugador pierde
# * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
# * - Puedes utilizar las palabras que quieras y el número de intentos que consideres

# Orden a seguir:
    # Elegir palabra y dar entre 2 - len(letras-1) letras de la palabra (random)
    # Usuario mete letra o palabra:
        # Si mete letra (1 char) si está en la palabra lo muestra, si no te quita un intento. 
        # Si mete una palabra (> 1 char) si es la palabra acaba el juego, si no te quita un intento
        # Si aciertas, has ganado -> GameOver (bien)
        # Si te quedas sin intento -> GameOver (mal)
    # Te pregunta si quieres volver a jugar

import random
import string
import typer

# He pedido a ChatGPT 40 palabras, para que no se repitan vaya
WORDS = ['manzana', 'platano', 'cereza', 'datil', 'zarzamora', 'uva', 'higo', 'sandia', 'limon', 'mango', 'naranja', 'pera', 'piña', 'frambuesa',
          'fresa', 'tangerina', 'pomelo', 'melon', 'albaricoque', 'arandano', 'coco', 'chirimoya', 'ciruela', 'granada', 'guayaba', 'kiwi', 'mandarina',
        'melocoton', 'membrillo', 'morango', 'nispero', 'papaya', 'piñon', 'queso', 'ruibarbo', 'tomate', 'vainilla', 'yogur', 'zanahoria']
TRIES = 3

def guess_answer():
    while True: # Para repetir el proceso hasta que el jugador de una respuesta correcta
        guess = input("Guess: ").lower()
        for l in set(guess):
            if l in string.digits:
                print("Solo pueden haber letras en la palabra")
                break
        if l in string.digits:
            continue
        if len(guess) == 0:
            print("Introduzca minimo 1 caracter")
            continue
        break
    return guess

def try_again():
    exit = typer.confirm("¿Quieres jugar otra partida?")
    if exit == 0:
        return 0

def main():
    print(f"¡Bienvenido al juego de adivinar las palabras! Tienes {TRIES} intentos por partida. ¡Disfruta!\n")
    while 1:
        answer = random.choice(WORDS)
        all_letters = list(set(answer))
        letters = list(random.choices(all_letters, k=random.randint(1, (len(all_letters)-1))))
        attempts = 0
        while attempts < TRIES:
            for i in answer:
                if i in letters:
                    print (i, end="")
                else:
                    print("_", end="")
            print(end="\n")
            if set(all_letters) == set(letters):
                print(f"¡Enhorabuena! Has encontrado el codigo en {attempts} intentos")
                break
            guess = guess_answer()
            if len(guess) == 1:
                if guess not in all_letters:
                    attempts += 1
                    print(f"Letra incorrecta, te quedan {TRIES-attempts} intentos")
                elif guess in letters:
                    print(f"Ya esta la letra colocada que haces bro")
                else:
                    letters.append(guess)
                    print(f"¡Letra correcta!")
            if len(guess) > 1 and guess == answer:
                print(f"¡Enhorabuena! Has encontrado el codigo en {attempts} intentos")
                break
            if len(guess) > 1 and guess != answer:
                attempts += 1
                print(f"Palabra incorrecta, te quedan {TRIES-attempts} intentos")
        else:
            print(f"Te quedaste sin intentos makena, la palabra correcta era '{answer}'")
        if try_again() == 0:
            break

if __name__ == "__main__":
    main()