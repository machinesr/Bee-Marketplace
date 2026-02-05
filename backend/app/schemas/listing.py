from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional
from .enums import ListingType, DigitalPayloadType

class ListingBase(BaseModel):
    title : str
    description: str
    listing_type: ListingType
    active : bool = True
    anonymous_sale: bool = False

class ListingCreate(ListingBase):
    stock: Optional[int] = None
    digital_payload_type: Optional[DigitalPayloadType] = None
    digital_payload_reference: Optional[str] = None


class ListingRead(ListingBase):
    id: UUID
    seller_id: UUID
    stock: Optional[int]
    digital_payload_type: Optional[DigitalPayloadType]
    digital_payload_reference: Optional[str]
    created_at: datetime
