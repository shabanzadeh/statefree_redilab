from fastapi import FastAPI
from routes.user import user

app = FastAPI()
app.include_router(user)


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}