from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    name: str
    username: str
    email: str
    preferred_language: str | None = None
    experience_level: str | None = None
    
class UserCreate(UserBase):
    password: str   
    
    
class UserUpdate(BaseModel):
    name: str | None = None
    username: str | None = None
    email: str | None = None
    preferred_language: str | None = None
    experience_level: str | None = None
    
class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    created_at: datetime
    updated_at: datetime