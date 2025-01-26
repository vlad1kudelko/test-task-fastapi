from pydantic import BaseModel

class Organisation(BaseModel):
    name: str
    phone: list[str]
    building_address: str
    building_position_x: float
    building_position_y: float
