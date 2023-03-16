### Users DB API ###

from fastapi import APIRouter, HTTPException
from models.models import User # From la carpeta.archivo(py) import el modelo
from client import db_client # Conexión a la base de datos (es la variable que creabamos en el archivo client)


router = APIRouter()

# Ahora esta lista que haciamos es inutil
users_list = []

@router.post("/user/", response_model=User, status_code=201) # Para crear el usuario en la base de datos
async def user(user: User):
    user_dict = dict(user) # Lo transformamos a un diccionario para introducirlo en la DB
    del user_dict("id") # Lo eliminamos (para que mongo cree uno, y usaremos ese)
    id = db_client.local.users.insert_one(user_dict).inserted_id # Insertamos el usuario, y a parte nos guardamos el id que crea el mondongo este

    db_client.local

    return user

@router.get("/users")
async def users():
    return users_list


@router.get("/user/{id}")  # Path
async def user(id: int):
    return search_user(id)


@router.get("/user/")  # Query
async def user(id: int):
    return search_user(id)


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user


@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}