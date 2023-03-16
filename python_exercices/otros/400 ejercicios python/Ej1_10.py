#1 Diseña un algoritmo para calcular el área de un círculo dado su radio. (área círculo == π veces el cuadrado del radio)

# import library_name --> library_name.specific_module() al llamarla
# from library_name import specific_module --> specific_module() al llamarla

from math import pi, pow

def func_area_circulo(r):
    return (pi*(pow(r,2)))

radio = 2
#radio = int(input())
print(func_area_circulo(radio))

#2 Diseña un algoritmo que calcule el IVA (16%) de un producto dado su precio de venta sin IVA

def func_iva(p):
    return (p*0.16)

print(func_iva(10))

#3 Diseña un programa que, a partir del valor del lado de un cuadrado, muestre el valor de su perímetro (en metros) y el de su área (en metros cuadrados)

def func_per_area_cuadrado(l):
    return (l*4, l*l)

print(func_per_area_cuadrado(3))

#4 Diseña un programa que, a partir del valor de la base y de la altura de un triángulo, muestre el valor de su área (en metros cuadrados)

def func_area_triangulo(b, h):
    return ((b*h)/2)

print (func_area_triangulo(3, 5))

#5 Diseña un programa que, a partir del valor de los dos lados de un rectángulo, muestre el valor de su perímetro (en metros) y el de su área (en metros cuadrados)

def func_per_area_rectangulo(l1, l2):
    return (2*(l1 + l2), l1*l2)

print(func_per_area_rectangulo(4, 6))

#6 Diseña un programa que pida el valor del lado de un cuadrado y muestre el valor de su perímetro y el de su área.

lado_cuadrado = 1.1
#lado_cuadrado = float(input())
a,b = func_per_area_cuadrado(lado_cuadrado)
print((a, round(b, 2)))

#7 Diseña un programa que pida el valor de los dos lados de un rectángulo y muestre el valor de su perímetro y el de su área

lado1_rectangulo = 1
lado2_rectangulo = 5
#lado1_rectangulo = float(input())
#lado2_rectangulo = float(input())
print(func_per_area_rectangulo(lado1_rectangulo, lado2_rectangulo))

#8 Diseña un programa que pida el valor de la base y la altura de un triángulo y muestre el valor de su área.

base_triangulo = 10
altura_triangulo = 100
#base_triangulo = float(input())
#altura_triangulo = float(input())
print(func_area_triangulo(base_triangulo, altura_triangulo))

#9 Diseña un programa que pida el valor de los tres lados de un triángulo y calcule el valor de su área y perímetro.

from math import sqrt

def func_area_triangulo_lados(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    return (s*2, sqrt(s*(s - l1)*(s - l2)*(s - l3)))

print(func_area_triangulo_lados(3, 5, 7))

#10 El área A de un triángulo se puede calcular a partir del valor de dos de sus lados, a y b, y del ángulo θ que éstos forman entre sí con la fórmula A = (1/2)*a*b*sin(angulo)
# Diseña un programa que pida al usuario el valor de los dos lados (en metros), el ángulo que estos forman (en grados), y muestre el valor del área (sin funciona con rad en python, pi = 180)

from math import sin

def func_area_triangulo_lados_angulo(l1, l2, angulo):
    return ((1/2)*l1*l2*sin(angulo*(pi/180)))

lado1_triangulo = 1
lado2_triangulo = 2
angulo_triangulo = 30
#lado1_triangulo = float(input())
#lado2_triangulo = float(input())
#angulo_triangulo = float(input())
print(func_area_triangulo_lados_angulo(lado1_triangulo, lado2_triangulo, angulo_triangulo))