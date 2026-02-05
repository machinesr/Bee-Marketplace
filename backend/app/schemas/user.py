from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    display_name: str
    anonymous_alias : str | None = None

class UserRead(UserBase):
    id : UUID
    created_at: datetime