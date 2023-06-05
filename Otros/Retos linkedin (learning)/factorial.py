# Factorial: dado un numero multiplicar el numero hasta 1 (5! = 5*4*3*2(*1 xd), negativo = None, 0! = 1)
# De forma recursiva

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
