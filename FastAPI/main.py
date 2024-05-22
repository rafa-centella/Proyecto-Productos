# Importamos lo que vamos a necesitar.
from fastapi import FastAPI
from routers import user

# Se define variable que almacenara el FastAPI.
app = FastAPI()

app.include_router(user.router)

# EndPoint de entrada en la API.
@app.get("/")
async def root():
    return "¡Bienvenido a la fantastica API! Desarrollada por Juan Jose Barroso Hidalgo y Rafael Centella Guijarro. Una Tienda con Productos y Usuarios."