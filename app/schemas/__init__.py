from pydantic import BaseModel, Field

class Organisation_schemas(BaseModel):
    name: str         = Field(..., title='Название организации',                example='ООО “Рога и Копыта”')
    phone: str        = Field(..., title='Номера телефонов',                    example='2-222-222, 3-333-333, 8-923-666-13-13')
    address: str      = Field(..., title='Адрес',                               example='г. Москва, ул. Ленина 1, офис 3')
    position_x: float = Field(..., title='Географические координаты (широта)',  example=55.717435)
    position_y: float = Field(..., title='Географические координаты (долгота)', example=37.561014)
