# Autentificación mas segura (OAuth2 JWT)
# Ahora usaremos un token JWT (token encriptado)

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from jose import jwt, JWTError # pip install "python-jose[cryptography]"
from passlib.context import CryptContext # pip install "passlib[bcrypt]"

from datetime import datetime, timedelta # Para trabajar con el tiempo maximo de inicio de sesion (ACCESS_TOKEN_DURATION)
# datetime => para la fecha del sistema (cuando se genere el token), timedelta => para trabajar con calculos de fecha

# También lo que se usa es un refresh token, para que si nos suplantan, que solo puedan tener x tiempo limite, mientras que si eres
# tú realmente puedas refrescar el token tranquilamente

# Los pasos a seguir para leer tus datos: 
    # Iniciar sesion en "/login" en "Body->Form" (con POST), con campos "username" y "password" del usuario
    # Te devolverá en string el "access_token", que estará codificado y tiene un tiempo limite de 1 minuto de uso
    # Copiar y pegar ese string en el "Auth->Bearer"
    # Ya puedes ir al "/users/me" (haciendo el GET) y te dirá tus datos

ALGORITHM = "HS256" # Algoritmo para encriptar las contraseñas (Este es el mas utilizado)
# La contraseña en la base de datos es la que ira encriptada con este seguro (pa que no se vea a simple vista vaya)
SECRET = "fc13e68d91dbba6c57e6aa15d6f511a8d2e4f4a4adbc90053d13170f1f2486a5" # He generado una semilla aleatoria ("openssl rand -hex 32") 
# (iba en la libreria passlib se supone, lo que hace es generar 32 caracteres alphanumericos)
# Esto se hace para que sea mas dificil desencriptar el access_token, para que solo lo sepa el backend, nadie mas, y asi será mas seguro
ACCESS_TOKEN_DURATION = 1 # Ahora, tendrás una duración con la sesion iniciada
# Cuando pase el tiempo (en este caso 1 minuto) tendrás que volver a iniciar la sesión y te generará otro token nuevo

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login") # Seguiremos usando user/password, pero ahora usaremos criptografia (token-sistema autentificación mas seguro)

crypt = CryptContext(schemes=["bcrypt"]) # Verificar la contraseña de la DB encriptada (contexto de encriptación)
# Schemes (esquemas), definen los algoritmos de encripcación que vamos a usar (en este caso bcrypt)
# (se pueden incluso pasar mas parametros para que haga mas cosas, pero por ahora simplón)
# Funciona de una manera muy concreta, pero nos la suda, se encargará ella de encriptar
# Es capaz de encriptar, pero no hacer la desencriptación (cacho segura vamo)

class User(BaseModel):
    user: str
    email: str | None = None
    disabled: bool | None = None

class UserDB(User):
    password: str

users_db = {
    "Paco33":{
        "user": "Paco33",
        "email": "paco33@gmail.com",
        "disabled": True,
        "password": "$2a$12$V15J8xLZtHkJdCbhfV9vH.MZR8DQmM8/haFSA05n1kWPLXSlKy7j2"
        # He pasado la contraseña por un generador bcrypt (contaseña = 1234)
    },
    "Juan21":{
        "user": "Juan21",
        "email": "eljuanox@gmail.com",
        "disabled": False,
        "password" : "$2a$19$OsE02xSQeiH56Ctsfu0wneVHxNBsC7zpeS6LaT1m1id2a7myF16de"
        # He pasado la contraseña por un generador bcrypt (contaseña = abcd)
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)): # Lo que usaremos para desencriptar el token y que de el user
    excepcion = HTTPException(status_code=401) # (Creamos nuestra variable para reusar esta excepcción (comodidad a tope))
    try:
        userjwt = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        # desencriptamos el token y nos da el archivo json con los parametros del usuario, y cogemos el "sub" (el user vamos)
        if userjwt == None:
            raise excepcion
    except JWTError: # Que ha petado
            raise excepcion
    # Si continua por aqui es que todo ha ido bien
    return search_user(userjwt) # Buscamos en la DB el user descifrado y lo devolvemos

async def current_user(user: User = Depends(auth_user)): # Ahora cambia el sistema, pondremos el Depends, y donde desencriptaremos el token para encontrar el user
    # y aqui devolveremos el user (es un poco cutre, pero lo puedes usar para otra cosa no solo para return user)
    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    my_user = users_db.get(form.username)
    if not my_user:
        raise HTTPException(status_code=400, detail="usuario incorrecto")
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password): # Mira si la contraseña introducida coincide con la contraseña de la base de datos
        # de la forma de crypt. (bcrypt en este caso) y lo verifica (desencriptando el hash de la password de la DB)
        raise HTTPException(status_code=400, detail="contraseña incorrecta")

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    # Fecha y hora de expiración = fecha y hora actual + tiempo que queremos que dure la sesion iniciada (y lo ponemos de clase timedelta para poder sumarlo)

    # Ahora generaremos un token, pero de una forma diferente, crearemos un archivo jsn con varios parametros del usuario y luego lo encriptaremos
    access_token = {"sub": user.user, "exp": expire} # Por nomenclatura se ponen esos nombres (y pa que lo lea también creo)
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"} # Aqui encriptamos el token
    # Cuando usemos el token, el sistema solo ya sabrá si ha expirado o no

@app.get("/users/me")
async def me(user: User = Depends(current_user)): # Depende() de si el current_user lo da por autenticado o no
    return user # Devuelve el user encontrado en el current_user