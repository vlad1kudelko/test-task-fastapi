from app.db.database import async_session_maker
from fastapi import FastAPI
from geopy.distance import great_circle
from sqlalchemy import select

from app.db.models import *
from app.schemas import *

app = FastAPI()

def get_organisation():
    return select(
        Organisation.name,
        Organisation.phone,
        Building.address,
        Building.position_x,
        Building.position_y,
    ).join(Building, Organisation.id_building == Building.id)

@app.get('/organisation-in-building')
async def api_building(building: int) -> list[Organisation_schemas]:
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

@app.get('/organisation-in-activity')
async def api_activity(activity: int) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        query = get_organisation().join(
            Link_org_act, Organisation.id == Link_org_act.id_org
        ).filter(Link_org_act.id_act == activity)
        results = (await session.execute(query)).all()
        return results

@app.get('/organisation-by-position')
async def api_position(x: float, y: float, radius: float) -> list[Organisation_schemas]:
    async with async_session_maker() as session:
        query = get_organisation()
        results = (await session.execute(query)).all()
        results_filter = [ org for org in results if great_circle(
            (x, y), (org.position_x, org.position_y)
        ).km <= radius ]
        return results_filter

@app.get('/organisation-by-id')
async def api_byid(id_organisation: int) -> Organisation_schemas:
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

@app.get('/organisation-by-name')
async def api_byname(name: str) -> list[Organisation_schemas]:
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
