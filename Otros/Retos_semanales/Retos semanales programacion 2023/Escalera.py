# * Crea una función que dibuje una escalera según su número de escalones.
# * - Si el número es positivo, será ascendente de izquiera a derecha.
# * - Si el número es negativo, será descendente de izquiera a derecha.
# * - Si el número es cero, se dibujarán dos guiones bajos (__).
# * 
# * Ejemplo: 4
# *         _
# *       _|       
# *     _|
# *   _|
# * _|
# * 

def escalones(n):
    if n == 0:
        print("__")
    if n < 0:
        print("_")
        i = 0
        while i > n+1:
            print(" ", end="")
            print(-i*"  " + "|_")
            i -= 1
        print(" "+-i*"  "+"|_")
    if n > 0:
        print(n*"  "+"_")
        while n > 1:
            n -= 1
            print(n*"  " + "_|")
        print("_|")

escalones(0)
print("----------------------------------------")
escalones(7)
print("----------------------------------------")
escalones(-7)