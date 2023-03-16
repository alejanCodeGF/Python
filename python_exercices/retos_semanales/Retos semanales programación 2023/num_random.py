# Crea un generador de números pseudoaleatorios entre 0 y 100.
# No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
# Es más complicado de lo que parece...


from datetime import datetime

# Mi idea es un poco como funciona el random, que es con la hora actual del reloj (microsegundos)

def num_rand_cero_cien():
    time = datetime.utcnow()
    numrand = 0
    if time.microsecond//1000 == 100:
        numrand = 100
    else:
        numrand = time.microsecond%100
    print(numrand)

num_rand_cero_cien()