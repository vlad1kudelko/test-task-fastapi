from app.db.database import async_session_maker
from fastapi import FastAPI
from sqlalchemy import select

from app.db.models import *
from app.schemas import *

app = FastAPI()

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
        query = select(
            Organisation.name,
            Organisation.phone,
            Building.address,
            Building.position_x,
            Building.position_y,
        ).join(
            Building, Organisation.id_building == Building.id
        ).join(
            Link_org_act, Organisation.id == Link_org_act.id_org
        ).filter(Link_org_act.id_act == activity)
        results = (await session.execute(query)).all()
        return results
