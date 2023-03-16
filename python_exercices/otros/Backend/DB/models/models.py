# Para simplificar, y poner aqui todos los modelos que vayamos a utilizar

from pydantic import BaseModel

class User(BaseModel):
    id: str | None # En mongo, el int será str (asi se pueden poner numeros mucho mas grandes)
    full_name: str
    email: str