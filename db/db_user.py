from schemas.user import User
from db.hash import Hash
from config.db import collection
from fastapi import HTTPException
from fastapi import status

async def create_user(request: User):
    user_data = User(
        name=request.name,
        password=Hash.bcrypt(request.password),
        email=request.email
    ).dict()
    
    result = await collection.insert_one(user_data)
    user_data["_id"] = str(result.inserted_id) 
    
    return user_data


async def get_user_by_username(name: str):
    user_dict = await collection.find_one({"name": name})
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found!")
    user_dict["_id"] = str(user_dict["_id"]) 
    return User(**user_dict)
