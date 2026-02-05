from uuid import UUID
from app.repositories.listing_repository import ListingRepository
from app.schemas.listing import ListingRead

class ListingService:
    def __init__(self, listing_repo: ListingRepository):
        self.listing_repo = listing_repo

    def get_listing(self, listing_id: UUID) -> ListingRead:
        listing = self.listing_repo.get_by_id(listing_id)

        if not listing:
            raise ValueError("no listing ")
        
        if not listing.active:
            raise ValueError("shi not acitve")
        
        return listing