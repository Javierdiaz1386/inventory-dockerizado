from pydantic import BaseModel
from bson import ObjectId

class Inventory(BaseModel):
    id_product : ObjectId
    stock : int
