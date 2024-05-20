from fastapi import FastAPI, Request
from routes.user import user
#from middeleware import auth
#from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

#app.add_middleware(BaseHTTPMiddleware, dispatch=auth.auth_middleware)

app.include_router(user)


