from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn users:app --reload

#Entidad User
class User(BaseModel):
    name: str
    aP: str
    url: str
    age: int

Users_list = [User(name="Adrian", aP="Torres", url="http://moure.dev", age=16),
            User (name="gustom", aP= "Morales",  url= "http://moure.com", age= 18),
            User (name="José", aP="gustoma", url="http://haakon.com", age=21)]
@app.get("/usersjson")
async def usersjson():
    return [{"name":"Adrian", "aP": "Torres",  "url": "http://moure.dev", "age": 16},
            {"name": "gustom", "aP": "Morales",  "url": "http://moure.com","age": 18},
            {"name": "José", "aP": "gustoma",  "url": "http://haakon.com", "age": 21}]

@app.get("/usersclass")
async def usersclass():
    return Users_list