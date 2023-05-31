# * Crea una función que reciba un número decimal y lo trasforme a Octal
# * y Hexadecimal.
# * - No está permitido usar funciones propias del lenguaje de programación que
# * realicen esas operaciones directamente.

# Decimal: 0,1,2,3,4,5,6,7,8,9,   10,11...
# Octal: 0,1,2,3,4,5,6,7,   10,11,12,13... (de 8 en 8 vaya, y el 10 en octal es el 8 en decimal)
# Hexadecimal: 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,   10,11,12... (Cuando acabe el decimal, letras hasta el 16, y luego se le añade un 1 delante, luego un 2...)

def trans_oct_hex(n):
    n_oct = str((n//8)*10 + n%8) # Dividimos entre 8, y luego por 10 (cifra delante), y le sumamos el residuo
    lista_letra = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n_hex = ''
    if n//16 > 0:
        n_hex = str((n//16))
    n_hex += lista_letra[n%16]
    return n_oct, n_hex

print(trans_oct_hex(31))