# Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
# - "X" si han ganado las "X"
# - "O" si han ganado los "O"
# - "Empate" si ha habido un empate
# - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
# Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.

# Entiendo que das 3 lineas de input, con listas
# Para que la proporcion sea correcta, tiene que ser 4 de una y 5 de otra

def cont_x_o(l1,l2,l3):
    dict = {}
    for i in l1:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in l2:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in l3:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    if dict["X"] >= 6 or dict["O"] >= 6:
        return 1
    return 0


def tic_tac_toe(l1, l2, l3):
    Vx = 0 # Victoria del X
    Vo = 0 # Victoria del O
    if cont_x_o(l1,l2,l3):
        return ("Null")
    if set(l1) == set("X") or set(l2) == set("X") or set(l3) == set("X"):
        Vx += 1
    if set(l1) == set("O") or set(l2) == set("O") or set(l3) == set("O"):
        Vo += 1
    for i in range(3):
        if l1[i] == "X" and l2[i] == "X" and l3[i] == "X":
            Vx += 1
        if l1[i] == "O" and l2[i] == "O" and l3[i] == "O":
            Vo += 1
    if l1[0] == "X" and l2[1] == "X" and l3[2] == "X":
        Vx += 1
    if l1[2] == "X" and l2[1] == "X" and l3[0] == "X":
        Vx += 1
    if l1[0] == "O" and l2[1] == "O" and l3[2] == "O":
        Vo += 1
    if l1[2] == "O" and l2[1] == "O" and l3[0] == "O":
        Vo += 1
    if Vx == 1 and Vo == 0:
        return("X")
    elif Vx == 0 and Vo == 1:
        return("O")
    elif Vx == 0 and Vo == 0:
        return("Empate")
    else: 
        return("Null")

# Plan:
    # Puede haber linea si l1, l2 o l3 son completamente "X" o "O", si l1[i], l2[i], l3[i] también son completados (y siempre el mismo "i" (1,2 o 3)) 
    # o si pasa con las diagonales (l1[1], l2[2], l3[3] y l1[3], l2[2], l3[1])

# Tests:
print(tic_tac_toe(["O", "O", "X"],["O", "X", "O"],["X", "O", "O"])) # Null (no hay proporción x y o)
print(tic_tac_toe(["X", "O", "X"],["X", "X", "O"],["O", "X", "O"])) # Empate
print(tic_tac_toe(["X", "X", "X"],["X", "O", "O"],["O", "O", "O"])) # Null (Gana x y o)
print(tic_tac_toe(["X", "O", "X"],["X", "O", "O"],["X", "X", "O"])) # Gana X
