# Haz un programa que pida al usuario una cantidad de euros, una tasa de interés y un número de años.
#1 Muestra por pantalla en cu´anto se habr´a convertido el capital inicial transcurridos esos a˜nos si cada a˜no se aplica la tasa de inter´es introducida

def func_interes_compuesto(c, i, a):
    while (a > 0):
        c = c*((i/100) + 1)
        a -= 1
    return (c)

print(func_interes_compuesto(10000, 4.5, 20))

#2 Haz un programa que pida el nombre de una persona y lo muestre en pantalla repetido 100 veces, pero dejando un espacio de separación entre aparición y aparición del nombre
# (Utiliza los operadores de concatenación y repetición.)

def func_repetir_nombre(name):
    name += " "
    name *= 100
    return (name)

var_nombre = "Paco"
#var_nombre = input()
print(func_repetir_nombre(var_nombre))


#3 Diseña un programa que solicite el radio de una circunferencia y muestre su área y perímetro con sólo 2 decimales

from Ej1_10 import func_area_circulo

def func_area_circulo_V2(r):
    return(round(func_area_circulo(r), 2))

radio = 1
#radio = float(input())
print(func_area_circulo_V2(radio))

#4 Diseña un programa que lea un número flotante por teclado y muestre por pantalla "N" si el numero es negativo y "P" si es positivo

def func_signo(x):
    if x >= 0:
        return ("P")
    else:
        return ("N")

var_numero = 2
#var_numero = float(input())
print(func_signo(var_numero))

#5 Diseña un programa que lea la edad de dos personas y diga quién de los dos es más joven (pueden tener la misma edad, hazlo saber con un mensaje adecuado)

def func_mayor_menor(n1, n2):
    if n1 > n2:
        print("La primera persona es mayor")
    elif n1 < n2:
        print("La segunda persona es mayor")
    else:
        print("ambos tienen la misma edad")

func_mayor_menor(23, 21)

#6 Diseña un programa que, dado un número entero, muestre por pantalla "El numero es par", si es par, y "El numero es impar", si es impar

def func_par_impar(n):
    if n % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

#7 Diseña un programa que, dado un número entero, determine si éste es el doble de un número impar o par

def func_mitad_impar(n):
    if n % 2 != 0:
        print("Este numero no vale, la mitad es decimal")
    else:
        func_par_impar(n/2)


func_mitad_impar(14)

#8 Diseña un programa que, dados dos números enteros, muestre por pantalla uno de estos mensajes: "El segundo es exactamente el cuadrado del primero", "El segundo es menor que el cuadrado del primero", "El segundo es mayor que el cuadrado del primero"

def func_comparacion_cuadrados(n1, n2):
    n1 = n1 * n1
    if n1 < n2:
        print("El segundo es mayor que el cuadrado del primero")
    elif n1 > n2:
        print("El segundo es menor que el cuadrado del primero")
    else:
        print("El segundo es exactamente el cuadrado del primero")

func_comparacion_cuadrados(2, 4)

#9 == al del interes compuesto, pero comprueba si x es >= 0

def func_interes_compuesto_V2(c, i, a):
    if i >= 0:
        return func_interes_compuesto(c, i, a)
    else:
        print("Es imposible que el interes sea negativo")
        return c

print(func_interes_compuesto_V2(10000, 4.5, 20))

#10 Realiza un programa que calcule el desglose en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €

def func_desglose_precio(p):
    if p//500 >= 1:
        d = p//500
        if d > 1:
            print(d, "billetes de 500")
        else:
            print(d, "billete de 500")
        p -= d*500
    if p//200 >= 1:
        d = p//200
        if d > 1:
            print(d, "billetes de 200")
        else:
            print(d, "billete de 200")
        p -= d*200
    if p//100 >= 1:
        d = p//100
        if d > 1:
            print(d, "billetes de 100")
        else:
            print(d, "billete de 100")
        p -= d*100
    if p//50 >= 1:
        d = p//50
        if d > 1:
            print(d, "billetes de 50")
        else:
            print(d, "billete de 50")
        p -= d*50
    if p//20 >= 1:
        d = p//20
        if d > 1:
            print(d, "billetes de 20")
        else:
            print(d, "billete de 20")
        p -= d*20
    if p//10 >= 1:
        d = p//10
        if d > 1:
            print(d, "billetes de 10")
        else:
            print(d, "billete de 10")
        p -= d*10
    if p//5 >= 1:
        d = p//5
        if d > 1:
            print(d, "billetes de 5")
        else:
            print(d, "billete de 5")
        p -= d*5
    if p//2 >= 1:
        d = p//2
        if d > 1:
            print(d, "monedas de 2")
        else:
            print(d, "moneda de 2")
        p -= d*2
    if p//1 >= 1:
        d = p
        if d > 1:
            print(d, "monedas de 1")
        else:
            print(d, "moneda de 1")
        p -= d*1

func_desglose_precio(889)
