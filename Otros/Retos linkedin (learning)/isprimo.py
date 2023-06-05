# Identificar si un numero es primo (hecho también en retos semanales 2022)

def num_primo(n):
    conprimo = 0
    if n == 1:
        return False
    if n > 0:
        for i in range(2, n + 1):
            if n % i == 0:
                conprimo += 1
        if conprimo == 1:
            return True
    return False

print(num_primo(2))

for i in range(101):
    if num_primo(i):
        print(i)