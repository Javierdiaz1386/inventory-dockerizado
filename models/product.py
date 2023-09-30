from pydantic import BaseModel

class Cerveza(BaseModel):
    price  : float
    name : str
    descripcion : str
    stock : int

