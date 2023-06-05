# Palindromo: que se lee igual de izquierda a derecha que de derecha a izquierda
# Obviando los espacios, y las mayusculas y minusculas son iguales

def is_palindromo(texto):
    texto_sin_espacios = ""
    for i in texto:
        if i != " ":
            texto_sin_espacios += i
    if texto_sin_espacios.lower() == texto_sin_espacios[::-1].lower():
        return True
    return False


print(is_palindromo("Anita lava la tina"))  # True
print(is_palindromo("Anita lava el baño"))  # False
