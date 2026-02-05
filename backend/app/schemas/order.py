from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from .enums import ListingType, StatusType
    
class OrderCreate(BaseModel):
    listing_id: UUID
   # quantity is left out for now because default to 1 in mvp

class OrderRead(BaseModel):
    id : UUID
    buyer_id: UUID
    seller_id: UUID
    listing_id: UUID
    listingType: ListingType
    status: StatusType
    delivered_at: datetime| None = None
    accepted_at: datetime | None  = None
    auto_complete_at: datetime | None = None
    created_at: datetime