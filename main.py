from app.db.database import async_session_maker
from fastapi import FastAPI
from geopy.distance import great_circle
from sqlalchemy import select

from app.db.models import *
from app.schemas import *

app = FastAPI(
    title='Тестовое задание по FastAPI',
    description='Документация к проекту',
    version='1.0.0',
)

def get_organisation():
    return select(
        Organisation.name,
        Organisation.phone,
        Building.address,
        Building.position_x,
        Building.position_y,
    ).join(Building, Organisation.id_building == Building.id)

@app.get('/organisation-in-building', summary='Список всех организаций находящихся в конкретном здании')
async def organisation_in_building(building: int) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        filtered_org = select(Organisation).filter(Organisation.id_building == building).subquery()
        query = select(
            filtered_org.c.name,
            filtered_org.c.phone,
            Building.address,
            Building.position_x,
            Building.position_y,
        ).join(Building, filtered_org.c.id_building == Building.id)
        results = (await session.execute(query)).all()
        return results

@app.get('/organisation-in-activity', summary='Список всех организаций, которые относятся к указанному виду деятельности')
async def organisation_in_activity(activity: int) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        query = get_organisation().join(
            Link_org_act, Organisation.id == Link_org_act.id_org
        ).filter(Link_org_act.id_act == activity)
        results = (await session.execute(query)).all()
        return results

@app.get('/organisation-by-position', summary='Список организаций, которые находятся в заданном радиусе относительно указанной точки')
async def organisation_by_position(x: float, y: float, radius: float) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        query = get_organisation()
        results = (await session.execute(query)).all()
        results_filter = [ org for org in results if great_circle(
            (x, y), (org.position_x, org.position_y)
        ).km <= radius ]
        return results_filter

@app.get('/organisation-by-id', summary='Информация об организации по её идентификатору')
async def organisation_by_id(id_organisation: int) -> Organisation_schemas:
    async with async_session_maker() as session:
        filtered_org = select(Organisation).filter(Organisation.id == id_organisation).subquery()
        query = select(
            filtered_org.c.name,
            filtered_org.c.phone,
            Building.address,
            Building.position_x,
            Building.position_y,
        ).join(Building, filtered_org.c.id_building == Building.id)
        result = (await session.execute(query)).first()
        return result

def recursion_activity(list_activity, id_activity, level):
    if level >= 4:
        return []
    list_ids = [act.id for act in list_activity if act.id_parent == id_activity]
    list_ret = [id_activity]
    for act_id in list_ids:
        list_ret += recursion_activity(list_activity, act_id, level+1)
    return list_ret

@app.get('/organisation-by-name-activity', summary='Список всех организаций, по виду деятельности с учетом вложенности')
async def organisation_by_name_activity(name: str) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        list_activity = (await session.execute(select(Activity.id, Activity.name, Activity.id_parent))).all()
        id_activity = [act for act in list_activity if act.name == name][0].id
        list_ids = recursion_activity(list_activity, id_activity, 1)
        query = get_organisation().join(
            Link_org_act, Organisation.id == Link_org_act.id_org
        ).filter(Link_org_act.id_act.in_(list_ids)).distinct()
        results = (await session.execute(query)).all()
        return results

@app.get('/organisation-by-name', summary='Поиск организации по названию')
async def organisation_by_name(name: str) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        filtered_org = select(Organisation).filter(Organisation.name == name).subquery()
        query = select(
            filtered_org.c.name,
            filtered_org.c.phone,
            Building.address,
            Building.position_x,
            Building.position_y,
        ).join(Building, filtered_org.c.id_building == Building.id)
        results = (await session.execute(query)).all()
        return results
