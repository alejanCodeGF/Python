
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
# - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
# - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"


def func_suc_fibonacci(n):
    listafibo = [0, 1]
    nfiboant = 0
    nfibo = 1
    vartemp = 0
    while nfibo < n:
        vartemp = nfibo
        nfibo = nfiboant+nfibo
        nfiboant = vartemp
        listafibo.append(nfibo)
    return listafibo

def func_primo_fibo_par(n):
    siesnoes = ["es primo,", "no es primo,", "fibonacci", "no es fibonacci", "y es par", "y es impar"]
    primo = 0 #+0 si es primo +1 si no lo es
    fibo = 2 #+0 si es fibo +1 si no lo es
    par = 4 #+0 si es par +1 si no lo es
    conprimo = 0
    if n % 2 != 0:
        par += 1
    if n == 1:
        primo += 1
        print(n, siesnoes[primo], siesnoes[fibo], siesnoes[par])
        return ()
    if n > 0:
        for i in range(2, n + 1):
            if n % i == 0:
                conprimo += 1
        if conprimo > 1:
            primo += 1
        if n not in func_suc_fibonacci(n):
            fibo += 1
    else:
        primo += 1
        fibo += 1
        if n == 0:
            fibo -= 1
    print(n, siesnoes[primo], siesnoes[fibo], siesnoes[par])
    return ()

for i in range(10):
    func_primo_fibo_par(i)