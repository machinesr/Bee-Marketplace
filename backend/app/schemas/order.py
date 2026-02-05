from pydantic import BaseModel
from uuid import UUID


class OrderCreate(BaseModel):
    listing_id: UUID
