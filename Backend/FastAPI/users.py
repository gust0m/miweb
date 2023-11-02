from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn users:app --reload

#Entidad User
class User(BaseModel):
    id: int
    name: str
    aP: str
    url: str
    age: int

Users_list = [User(id= 1,name="Adrian", aP="Torres", url="http://moure.dev", age=16),
            User (id= 2,name="gustom", aP= "Morales",  url= "http://moure.com", age= 18),
            User (id= 3,name="José", aP="gustoma", url="http://haakon.com", age=21)]
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Adrian", "aP": "Torres",  "url": "http://moure.dev", "age": 16},
            {"name": "gustom", "aP": "Morales",  "url": "http://moure.com","age": 18},
            {"name": "José", "aP": "gustoma",  "url": "http://haakon.com", "age": 21}]

#get de usuarios
@app.get("/usersclass")
async def users():
    return Users_list

#get de usuarios con try catch
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, Users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}