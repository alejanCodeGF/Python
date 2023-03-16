#Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...
#
# He preferido hacerlo que dado un numero n te de n numeros de fibonacci

def func_suc_fibo(n):
    nfiboant = 0
    nfibo = 1
    vartemp = 0
    print(nfiboant)
    while n > 0:
        print(nfibo)
        vartemp = nfibo
        nfibo = nfiboant + nfibo
        nfiboant = vartemp
        n -= 1

func_suc_fibo(50)