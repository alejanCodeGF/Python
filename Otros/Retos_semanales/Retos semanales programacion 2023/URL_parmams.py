# * Dada una URL con parámetros, crea una función que obtenga sus valores.
# * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# *
# * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# * los parámetros serían ["2023", "0"]

# Lo que entiendo es que los parametros van seguidos de un "=", y separados entre parametros por un "&"

def parametros_url(url):
    inicio = 0
    lista = []
    for pos in range(len(url)):
        if url[pos] == "=":
            inicio = pos + 1
        if url[pos] == "&":
            lista.append(url[inicio:pos])
            inicio = 0
    if inicio != 0:
        lista.append(url[inicio:len(url)])
    return lista

print(parametros_url("https://retosdeprogramacion.com?year=2023&challenge=0"))
