from uuid import UUID
from fastapi import APIRouter, Depends
from app.dependencies.listings import listing_service
from app.schemas.listing import ListingRead
from app.dependencies.auth import get_current_user

router = APIRouter(
    prefix="/listings",
    dependencies=[Depends(get_current_user)],
)

@router.get("/{listing_id}", response_model=ListingRead)

def get_listing(listing_id: UUID):
    return listing_service.get_listing(listing_id)