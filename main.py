from app.db.database import async_session_maker
from fastapi import FastAPI
from sqlalchemy import select

from app.db.models import *
from app.schemas import *

app = FastAPI()

@app.get('/organisation-in-building')
async def api_hello(building: int) -> list[Organisation_schemas]:
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
