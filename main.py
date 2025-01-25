from fastapi import FastAPI

app = FastAPI()

@app.get('/hello')
async def api_hello():
    return {'hello': 'world'}
