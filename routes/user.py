from fastapi import APIRouter,Depends, HTTPException, status
from schemas.user import User
from db.models import users_serializer
from config.db import collection
from datetime import timedelta
from db.hash import Hash
from jose import jwt




user = APIRouter(prefix="/user", tags=['user'])


@user.post("/register")
async def create_user(user: User):
    existing_user = collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    
    hashed_password = Hash.bcrypt(user.password)
    user.password = hashed_password
    
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": user}
 




@user.post("/login")
async def login_user(user: User):
    found_user = collection.find_one({"name": user.name, "email": user.email, "phone": user.phone})
    
    if not found_user:
        raise HTTPException(status_code=400, detail="User not found")
    
    if Hash.verify(user.password, found_user["password"]):
        return {"status": "login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")


@user.get("")
async def get_user(user: User):
    userdata =  collection.find({}, {"_id": 0})
    result_dicts = [doc for doc in userdata]
    return result_dicts

       

