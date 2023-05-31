# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

# De la forma que lo he hecho es: en morse letras separadas por espacios, y espacios separados por '/' (P.e: Que tal? -> --.- ..- . / - .- .-.. ..--.. (que se tiene que pensar de esta forma: Q U E / T A L))
# Y al reves lo mismo, detecta cada letra por los espacios, y cada palabra por los '/'

def func_natural_morse(t):
    lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
                    'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?', '/', '-', '(', ')']
    lista_morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', 
                    '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', 
                    '-....', '--...', '---..', '----.', '-----', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']
    dic_natural_morse = {} # Los hago separados, y luego hago el diccionario de una forma o otra depende de si esta en morse o en ASCII
    texto_final = ""
    if set(t).issubset(set(' ./-')): # Si está en morse
        lista_palabras = t.split(' ')
        i = (len(lista_palabras) - 1)
        while (i >= 0): # Para quitar espacios que igual son problematicos
            if lista_palabras[i] == '':
                lista_palabras.pop(i)
            i -= 1 # Lo recorro al revés porque si lo hago de 0 -> len, cuando elimino 1 da error (bus error)
        for i in range(len(lista_letras)):
            dic_natural_morse[lista_morse[i]] = lista_letras[i]
        for p in lista_palabras:
            if p == '/':
                texto_final += ' '
            else:
                texto_final += dic_natural_morse[p]
        return texto_final
    else: # Si esta en ASCII
        t = t.upper()
        lista_palabras = t.split(' ')
        for i in range(len(lista_letras)):
            dic_natural_morse[lista_letras[i]] = lista_morse[i]
        for pi in range(len(lista_palabras)):
            varstring = ""
            for letra in lista_palabras[pi]:
                varstring += dic_natural_morse[letra]
                varstring += ' '
            lista_palabras[pi] = varstring 
        texto_final = '/ '.join(lista_palabras)
        return texto_final

a = func_natural_morse("Que tal?")
b = func_natural_morse(a)
print(a)
print(b)