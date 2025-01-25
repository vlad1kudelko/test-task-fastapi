from pydantic import BaseModel

class Organisation(BaseModel):      # Организация - Представляет собой карточку организации в справочнике и должна содержать в себе следующую информацию
    name: str                       # Название: Например ООО “Рога и Копыта”
    phone: list[str] = []           # Номер телефона: организация может иметь несколько номеров телефонов (2-222-222, 3-333-333, 8-923-666-13-13)
    _id_building: int               # Здание: Организация должна находится в одном конкретном здании (Например, Блюхера, 32/1)
    _ids_activity: list[int] = []   # Деятельность: Организация может заниматься несколькими видами деятельностей (Например, “Молочная продукция”, “Мясная продукция”)

class Building(BaseModel):          # Здание - Содержит в себе как минимум информацию о конкретном здании
    _id_: int
    address: str                    # Адрес: Например - г. Москва, ул. Ленина 1, офис 3
    point: str                      # Географические координаты: Местоположение здания должно быть в виде широты и долготы

class Activity(BaseModel):          # Деятельность. Имеет название и может в древовидном виде вкладываться друг в друга
    _id_: int
    name: str
    _id_parent: int
