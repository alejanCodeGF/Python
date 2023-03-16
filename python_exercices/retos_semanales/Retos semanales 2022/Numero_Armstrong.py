# Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong.
# Un número Armstrong (también conocido como número narcisista o número pling-plong) es un número de n dígitos que es igual a la suma de las potencias n-ésimas de sus dígitos.
# P.e: 1³ + 5³ + 3³ == 153. Otro ejemplo es el número 371, ya que 3³ + 7³ + 1³ == 371.

def num_armstrong(n):
    n2 = n
    ldigitos = []
    while n2 != 0:
        if n2 <= 9:
            ldigitos.append(n2)
            n2 = 0
        else:
            ldigitos.append(n2%10)
            n2 = n2//10
    a = 0
    for i in ldigitos:
        a += i*i*i
    return a == n

print(num_armstrong(153))