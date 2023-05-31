# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

class Poligono:
    def __init__(self):
        self.area = 0
        self.forma = "poligono"

    def get_area(self):
        print(f"El area del poligono {self.forma} es: {self.area}")

class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.area = base * altura
        self.forma = "triangulo"

class Rectangulo(Poligono):
    def __init__(self, lado1, lado2):
        self.area = lado1 * lado2
        self.forma = "rectangulo"

class Cuadrado(Poligono):
    def __init__(self, lado):
        self.area = lado * lado
        self.forma = "cuadrado"

def func_area(p):
    p.get_area()
    return p.area

var_triangulo = func_area(Triangulo(10.0, 5.0))
var_rectangulo= func_area(Rectangulo(5.0, 7.0))
var_cuadrado= func_area(Cuadrado(4.0))

print(var_triangulo)
print(var_rectangulo)
print(var_cuadrado)