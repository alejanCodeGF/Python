# el triangulo ese de 1, 1 1, 1 2 1, 1 3 3 1, etc
# Dado un numero, devolver una lista con listas dentro de cada fila hasta el numero dado

def tr_pascal(n):
    i = 1
    s = 1
    lfin = []
    while i <= n:
        l = [1]*i
        if len(l) >= 3:
            for i in range(len(l)):
                i
