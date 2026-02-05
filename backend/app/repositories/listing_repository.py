from abc import ABC, abstractmethod
from app.schemas.listing import ListingRead
from uuid import UUID

class ListingRepository(ABC):

    @abstractmethod
    def get_by_id(self, listing_id : UUID) -> ListingRead | None:
        pass

    @abstractmethod
    def create(self, seller_id: UUID, data) -> ListingRead:
        pass

    @abstractmethod
    def update(self, listing_id: UUID, updates: dict):
        pass
    