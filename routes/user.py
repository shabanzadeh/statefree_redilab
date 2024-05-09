from fastapi import APIRouter
from fastapi.responses import JSONResponse
from bson import json_util
from models.user import User

from schemas.user import users_serializer
from bson import ObjectId
from config.db import collection

user = APIRouter(prefix="/user", tags=['user'])

@user.post("")
async def create_user(user: User):
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": user}

@user.get("")
async def get_user(user: User):
    userdata =  collection.find({}, {"_id": 0})
    result_dicts = [doc for doc in userdata]
    return result_dicts
    
       

