# recibe texto de la forma "Horas:Minutos AM" o "Horas:Minutos PM"
# return en formato 24 horas
# En el ejemplo lo hace sin espacio, yo lo hago con espacio, que pasa

def cambio_formato(texto):
    am_pm = texto[-2:].lower()
    # Si quieres que sea sin el espacio, poner 2 aquí abajo
    hora_min_str = texto[:-3]
    hora_min = hora_min_str.split(":")
    if am_pm == "am":
        hora_min[0] = str(int(hora_min[0]) - 12)
    elif am_pm == "pm":
        hora_min[0] = str(int(hora_min[0]) + 12)
    if hora_min[0] == "0":
        hora_min[0] = "00"
#    print(f"{hora_min[0]}:{hora_min[1]}")
    return ":".join(hora_min)


print(cambio_formato("12:00 aM"))
