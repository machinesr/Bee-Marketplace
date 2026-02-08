from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    display_name: str
    anonymous_alias : str | None = None

class UserRead(UserBase):
    id : UUID
    created_at: datetime

class UserUpdate(BaseModel):
    display_name: str | None = Field(default=None, min_length=3, max_length=20)
    