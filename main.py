from fastapi import FastAPI
from middleware.auth import auth_middleware
from routes.user import user

app = FastAPI()
app.include_router(user)
app.middleware('http')(auth_middleware)