from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user


app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=['3000'],
    allow_credentials=True, allow_methods=['*'], allow_headers=['*'])


app.include_router(user)

