from fastapi import FastAPI
from models.product import Cerveza
from db.db import client
from serializer.product_serializer import CervezaSerializer
from bson import ObjectId

app = FastAPI()

@app.get('/')
async def home() -> dict:
    return {
        "messague" : "This home API"
    }

@app.post('/product/create')
async def create_product(cerveza:Cerveza) -> dict:
    if(isinstance(client["product"].find_one({"name":cerveza.name}), dict)):
        return {"error" : "Ya hay un producto con este nombre"}
    else:
        id = client["product"].insert_one(cerveza.__dict__).inserted_id
        created = client["product"].find_one({"_id":id})
    return  CervezaSerializer(created)

@app.delete('/product/delete/{id:str}')
async def delete_product(id:str) -> dict:
    try:
        if(isinstance(client["product"].find_one({"_id": ObjectId(id)}), dict)):
            client["product"].delete_one({"_id": ObjectId(id)})
            return {"messague" : "producto eliminado" }

    except:
         return {"error" : "Este producto no existe."}
    
@app.put('/product/update/{id:str}')
async def update_product(cerveza:Cerveza, id:str) -> dict:
    update =  client["product"].update_one({'_id' : ObjectId(id)}, {"$set": cerveza.__dict__})
    return {"messague" : "Actualizado correctamente"}

@app.get('/product/list')
async def list_product() -> list:
    all = client["product"].find()
    all = [CervezaSerializer(i) for i in all]
    return all

