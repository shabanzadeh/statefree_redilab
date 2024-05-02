from pydantic import BaseModel 


class User(BaseModel):
    name: str
    email: str
    password: str
    
class UserDisplay(BaseModel):
    name: str
    email: str