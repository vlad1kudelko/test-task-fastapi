from pydantic import BaseModel

class Organisation_schemas(BaseModel):
    name: str
    phone: str
    address: str
    position_x: float
    position_y: float
