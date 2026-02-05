from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class SellerProfileBase(BaseModel):
    is_anonymous_by_default: bool = False

class SellerProfileCreate(SellerProfileBase):
    payout_provider: str
    payout_reference_id: str

class SellerProfileRead(SellerProfileBase):
    id: UUID
    user_id: UUID
    payout_provider: str
    created_at: datetime

