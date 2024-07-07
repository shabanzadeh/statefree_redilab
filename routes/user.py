from bson import ObjectId
from fastapi import APIRouter, HTTPException, status, Depends, UploadFile
import shutil
from db.models import users_serializer
from schemas.user import User, UserLogin
from config.db import collection
from db.hash import Hash
from jose import jwt
from utilities.helper import remove_field_document
from middelware.auth import auth_middleware
import os
from db.uploaded_files import save_file, retrieve_file

user = APIRouter(prefix="/user", tags=['user'])


@user.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    upload_folder = "uploaded_files"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    with open(f"uploaded_files/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    file_id = save_file(f"uploaded_files/{file.filename}", file.filename)
    os.remove(f"uploaded_files/{file.filename}")
    return {"filename": file.filename}


@user.post("/register")
async def create_user(user: User):
    existing_user = collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    hashed_password = Hash.bcrypt(user.password)
    user.password = hashed_password
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok", "data": user}


@user.post("/login")
async def login_user(user: UserLogin):
    found_user = collection.find_one({"name": user.name})

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")

    if Hash.verify(user.password, found_user["password"]):
        token = jwt.encode(
            {'sub': found_user["name"]}, "test", algorithm='HS256')
        return {"token": token}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")


@user.get("/{user_id}", dependencies=[Depends(auth_middleware)])
async def detail(user_id: str):
    try:
        user_obj_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID format")

    user_detail = collection.find_one({"_id": user_obj_id})
    if not user_detail:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Could not find user with given ID")

    user_remove = remove_field_document(user_detail, ["password"])
    user_remove["id"] = str(user_remove["_id"])
    user_remove.pop("_id", None)

    return user_remove


@user.get("")
async def get_user():
    userdata = collection.find({}, {"_id": 0})
    result_dicts = [doc for doc in userdata]
    return result_dicts
