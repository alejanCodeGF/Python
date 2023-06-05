# Dado un numero, darás la suma de los anteriores (fila 3 = 3 + 2 + 1 = 6)

def num_triangular(n):
    if n < 0:
        return
    f = n
    while n > 0:
        n -= 1
        f += n
    return f


print(num_triangular(2))
print(num_triangular(4))
print(num_triangular(6))
