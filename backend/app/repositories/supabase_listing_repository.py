from app.repositories.listing_repository import ListingRepository
from app.db.client import supabase
from app.schemas.listing import ListingRead
from uuid import UUID

class SupabaseListingRepository(ListingRepository):
    def get_by_id(self, listing_id: UUID) -> ListingRead | None:
        res = (
            supabase
            .table("listings")
            .select("*")
            .eq("id", str(listing_id))
            .limit(1)
            .execute()
        )
        return ListingRead(**res.data[0]) if res.data else None
    
    def create(self, data):
        pass

    def update(self, id, data):
        pass