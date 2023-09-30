from models.product import Cerveza

def CervezaSerializer(cerveza : Cerveza) -> dict:
    return {
        "price" : cerveza["price"],
        "name" : cerveza["name"],
        "descripcion" : cerveza["descripcion"],
        "stock" : cerveza["stock"]           
    }