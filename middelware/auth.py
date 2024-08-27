from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


async def auth_middleware(request: Request, call_next):
    try:
        credentials: HTTPAuthorizationCredentials = await security(request)
        token = credentials.credentials
        payload = jwt.decode(token, "test", algorithms=["HS256"])
        request.state.user = payload
    except JWTError:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail": "Token is invalid or expired"}
        )

    response = await call_next(request)
    return response


async def auth_middleware_username_return(request: Request):
    try:
        credentials: HTTPAuthorizationCredentials = await security(request)
        token = credentials.credentials
        payload = jwt.decode(token, "test", algorithms=["HS256"])
        return str(payload.get("sub"))
    except JWTError:
        raise HTTPException(
            status_code=403, detail="Token is invalid or expired")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Some error")


async def verify_admin_token(request: Request):
    try:
        credentials: HTTPAuthorizationCredentials = await security(request)
        token = credentials.credentials
        payload = jwt.decode(token, "test", algorithms=["HS256"])
        if payload.get("sub") != "admin_statefree":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized"
            )
        request.state.user = payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token is invalid or expired"
        )
