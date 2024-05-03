from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    name: str
    email: str
    password: str
    creat_at: datetime = Field(default_factory=datetime.utcnow)
    
class UserDisplay(BaseModel):
    name: str
    email: str
    class Config:
        orm_mode = True