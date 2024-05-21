from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from jose import jwt
#from dotenv import load_dotenv
import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


#load_dotenv()
#SECRET_KEY = os.getenv("SECRET_KEY")
#print(SECRET_KEY)




security = HTTPBearer()

async def auth_middleware(request: Request, call_next):
  
    credentials: HTTPAuthorizationCredentials = await security(request)
    token = credentials.credentials
    payload = None
    try:
        payload = jwt.decode(token, "test", algorithms=["HS256"])
        request.state.user = payload
        
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "Token is invalid or expired"}
        )
    
    if not payload:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "Token is invalid or expired"}
        )
  
    response = await call_next(request)
    return response




