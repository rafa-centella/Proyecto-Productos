# Importamos lo que vamos a necesitar.
from fastapi import FastAPI
from routers import login, users, product, orders

# Se define variable que almacenara el FastAPI.
app = FastAPI()


app.include_router(login.router)
app.include_router(users.router)
app.include_router(product.router)
app.include_router(orders.router)

# EndPoint de entrada en la API.
@app.get("/")
async def root():
    return {"Bienvenido a FastAPI": "¡Magnifico Proyecto!, Una Tienda con Productos y Usuarios. Desarrollada por Juan Jose Barroso Hidalgo y Rafael Centella Guijarro."}


#{"id":"6650c7e3dcd30ce988835b97", "username": "Rafa", "password": "$2a$12$HK73aLtJQ0Go82dN4k1zIO477jvYGAWj8oaquFDqJ1kp9mp541A9S", "email": "rafa@localhost.com", "is_admin": false}

