from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class Organisation(Base):            # Организация - Представляет собой карточку организации в справочнике и должна содержать в себе следующую информацию
    __tablename__ = 'organisation'
    id:           Mapped[int]        = mapped_column(BigInteger, primary_key=True, index=True)
    name:         Mapped[str]                                                                        # Название: Например ООО “Рога и Копыта”
    phone:        Mapped[str]                                                                        # Номер телефона: организация может иметь несколько номеров телефонов (2-222-222, 3-333-333, 8-923-666-13-13)
    id_building:  Mapped[int | None] = mapped_column(ForeignKey('building.id'))                      # Здание: Организация должна находится в одном конкретном здании (Например, Блюхера, 32/1)
    link_org_act                     = relationship('Link_org_act')

class Link_org_act(Base):            # Организация может заниматься несколькими видами деятельностей (Например, “Молочная продукция”, “Мясная продукция”)
    __tablename__ = 'link_org_act'
    id:           Mapped[int]        = mapped_column(BigInteger, primary_key=True, index=True)
    id_org:       Mapped[int]        = mapped_column(ForeignKey('organisation.id'))
    id_act:       Mapped[int]        = mapped_column(ForeignKey('activity.id'))

class Building(Base):                # Здание - Содержит в себе как минимум информацию о конкретном здании
    __tablename__ = 'building'
    id:           Mapped[int]        = mapped_column(BigInteger, primary_key=True, index=True)
    address:      Mapped[str]                                                                        # Адрес: Например - г. Москва, ул. Ленина 1, офис 3
    position_x:   Mapped[float]                                                                      # Географические координаты: Местоположение здания должно быть в виде широты и долготы
    position_y:   Mapped[float]                                                                      # Географические координаты: Местоположение здания должно быть в виде широты и долготы
    organisation                     = relationship('Organisation')

class Activity(Base):                # Деятельность. Имеет название и может в древовидном виде вкладываться друг в друга
    __tablename__ = 'activity'
    id:           Mapped[int]        = mapped_column(BigInteger, primary_key=True, index=True)
    name:         Mapped[str]
    id_parent:    Mapped[int | None] = mapped_column(ForeignKey('activity.id'))
    link_org_act                     = relationship('Link_org_act')
    activity                         = relationship('Activity')
