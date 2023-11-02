from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url: https://mouredev.com/python"}

#Inicia el server: uvicorn main:app --reload
#Detener el server: ctrl + C

