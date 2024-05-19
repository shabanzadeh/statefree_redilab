from fastapi import APIRouter,Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import User
from db.models import users_serializer
from config.db import collection
from datetime import timedelta


user = APIRouter(prefix="/user", tags=['user'])


@user.post("/register")
async def create_user(user: User):
    existing_user = collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User alerady exists")
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": user}


@user.get("")
async def get_user(user: User):
    userdata =  collection.find({}, {"_id": 0})
    result_dicts = [doc for doc in userdata]
    return result_dicts

       

