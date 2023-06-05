# Dado una URL, devolver lo mismo pero sin caracteres no alphanumericos
# Los espacios son remplazados por guion

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnñopqrstuvxyz"
NUM = "0123456789-"


def slugfy(texto):
    t_final = ""
    for i in texto:
        if i in ALPHA:
            t_final += i.lower()
        elif i in NUM:
            t_final += i
        elif i == " ":
            t_final += "-"
    return t_final


print(slugfy("holA como sta-..-,.,-x"))  # hola-como-sta---x
