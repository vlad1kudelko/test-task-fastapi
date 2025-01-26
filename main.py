from fastapi import FastAPI

from app.schemas import Organisation

app = FastAPI()

@app.get('/organisation-in-building')
async def api_hello(building: int) -> list[Organisation]:
    return {'hello': 'world'}
