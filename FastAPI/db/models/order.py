from pydantic import BaseModel

class Order(BaseModel):
    id: str | None
    cod_order: int
    username: str
    id_product: str
