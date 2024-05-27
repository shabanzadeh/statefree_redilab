from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from routes.user import user


app = FastAPI()
app.include_router(user)

