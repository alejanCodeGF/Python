# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def func_dec_bin(ni):
    n = ni
    numfinal = ""
    if n <= 0: #He considerado captar el error de numeros negativos dandoles el valor de 0, también se podria hacer con el valor absoluto del numero y darselo en positivo por ejemplo
        return 0
    while n > 0:
        numfinal += f"{n % 2}"
        n = n // 2
    numfinal = numfinal[::-1]
    return int(numfinal)

def func_dec_bin_rec(n):
    if n < 2:
        if n <= 0:
            print(0)
            return ()
        print (1, end = "")
    else:
        func_dec_bin_rec(n // 2)
        print(n % 2, end = "")

for i in range(29):
    print(func_dec_bin(i))
func_dec_bin_rec(28)