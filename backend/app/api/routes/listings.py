from uuid import UUID
from fastapi import APIRouter
from app.dependencies.listings import listing_service
from app.schemas.listing import ListingRead

router = APIRouter()

@router.get("/listings/{listing_id}", response_model=ListingRead)
def get_listing(listing_id: UUID):
    return listing_service.get_listing(listing_id)