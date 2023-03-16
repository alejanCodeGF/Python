# Autenticación de forma basica

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Los pasos a seguir para leer tus datos: 
    # Iniciar sesion en "/login" en "Body->Form" (con POST), con campos "username" y "password" del usuario
    # Te devolverá en string el "access_token", que en este caso es sencillo pero tendrá que escar codificado
    # Copiar y pegar ese string en el "Auth->Bearer" (p.e: Paco33), ese es el token
    # Ya puedes ir al "/users/me" (haciendo el GET) y te dirá tus datos (que en este ejemplo es una chusta)

app = FastAPI()

@app.get("/")
async def inicio():
    return "Hola buenax"

def fake_hash_password(password: str): # Forma hiperpocha de cifrar una contraseña
    return "fakehashed" + password # No será asi vaya xd

oauth2 = OAuth2PasswordBearer(tokenUrl="login") # Criterio autentificación, con el URL donde iniciemos sesion (/login en esta web p.e)

class User(BaseModel): # Usuario, con la que trabajaremos (y enseñaremos al usuario)
    user: str
    email: str | None = None # Para indicar que los puedes dejar vacios estos campos
    disabled: bool | None = None # Si no pones nada se devolverá un null en esos campos

class UserDB(User): # Usuario en base de datos (con la contraseña, mas privado)
    password: str

users_db = {
    "Paco33":{
        "user": "Paco33",
        "email": "paco33@gmail.com",
        "disabled": True,
        "password": "fakehashed1234"
    },
    "Juan21":{
        "user": "Juan21",
        "email": "eljuanox@gmail.com",
        "disabled": False,
        "password" : "fakehashedabcd"
    }
}

def search_user_db(username: str): # Para encontrar la contraseña (en el post de "/login")
    if username in users_db:
        return UserDB(**users_db[username]) # Es un diccionario y lo "desempaquetas"
    
def search_user(username: str): # Para mostrar el usuario sin contraseña (current user, que es a su vez el get de "/users/me"(por el Depends))
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)): # Lo que tiene que cumplir para que el Depends te lo de por bueno (y en el caso de get devolver el usuario)
    # A su vez también depende de la variable oauth2 (sistema de autentificación, que ha gestionado un token de tipo Bearer que hemos obtenido en el /login)
    user = search_user(token) # Token que introducimos (Bearer Token en el Auth)
    if not user:
        raise HTTPException(status_code=401, detail="no estas autorizado")
    return user

@app.get("/login")
async def inicio():
    return "Introduce usuario y contraseña"

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    my_user = users_db.get(form.username) # Busca el usuario si esta
    if not my_user: # Si no lo encuentra
        raise HTTPException(status_code=400, detail="usuario incorrecto") # Usuario no encontrado
    user = search_user_db(form.username) # Si lo encuentra busca la contraseña en el db (busca el user entero y todos sus datos)
    if not form.password == user.password: # Si no coincide la contraseña
        raise HTTPException(status_code=400, detail="contraseña incorrecta") # Contraseña incorrecta
    return {"access_token": user.user, "token_type": "bearer"} # Si todo esta correcto has "iniciado sesion"

@app.get("/users/me")
async def me(user: User = Depends(current_user)): # Depende() de si el current_user lo da por autenticado o no
    return user # Devuelve el user encontrado en el current_user (que en este caso es un search_user(nombre_user) y lo encuentra)
    # Normalmente no serán tan senzillas, habrá que cifrarlos y to eso los tokens