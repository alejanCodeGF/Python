# Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.

import time

def stop_time(suma1, suma2, espera):
    time.sleep(espera)
    return suma1+suma2

print(stop_time(5, 6, 2))