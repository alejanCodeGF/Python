def func_balanced_delimiters(ex):
    lista_ex = []
    for char in ex:
        if char in '({[': # Si abre, lo mete en la lista
            lista_ex.append(char)
        elif char in ')}]': # Si cierra, comprueba la simetria
            if not lista_ex: # Si cierra antes que abre la lista, erroneo
                return False
            if char == ')' and lista_ex[-1] != '(':
                return False
            if char == '}' and lista_ex[-1] != '{':
                return False
            if char == ']' and lista_ex[-1] != '[':
                return False
            lista_ex.pop() # Y lo quita (ya ha cerrado)
    return not lista_ex # Si la lista esta vacia, correcto, si queda algun elemento, erroneo

l = ["{a + b [c] * (2x2)}", "{ [ a * ( c + d ) ] - 5 }", "{ a * ( c + d ) ] - 5 }", "{a^4 + (((ax4)}", "{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }", "{{{{{{(}}}}}}", "(a"]
for i in l:
    print(func_balanced_delimiters(i))