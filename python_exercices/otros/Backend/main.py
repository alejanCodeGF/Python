from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()

@app.get("/")
async def root():
    return 0
@app.get("/secreto")
async def root():
    return "Eto e un cecreto"


app2 = FastAPI()

class User(BaseModel):
    id: int
    nombre: str
    apellido1: str
    apellido2: str
    fecha_nacimiento: datetime

lista_users = [User(id=1, nombre="Pedro", apellido1="Jimenez", apellido2="Sancho", fecha_nacimiento=datetime(1996, 4, 8)),
User(id=2, nombre="Juan", apellido1="Jimenez", apellido2="Sancho", fecha_nacimiento=datetime(1992, 9, 4)),
User(id=3, nombre="Carlos", apellido1="Rubio", apellido2="Moreno", fecha_nacimiento=datetime(1996, 5, 2))]

@app2.get("/")
async def inicio():
    return lista_users
    return search_user(lista_users, 4)

@app2.post("/")
async def user(user: User):
    lista_users.append(user)

@app2.put("/")
async def cambiar_user(user: User, indice: int):
    lista_users[indice] = user

def search_user(l, id):
    for i in l:
        if i.id == id:
            return i
    return