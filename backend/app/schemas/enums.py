from enum import Enum

class ListingType(str, Enum):
    DIGITAL_ITEM = "digital_item"
    SERVICE = "service"

class DigitalPayloadType(str, Enum):
    FILE = "file"
    LINK = "link"
    TEXT = "text"

class StatusType(str, Enum):
    PENDING = "pending"
    DELIVERED = "delivered"
    ACCEPTED = "accepted"
    DISPUTED = "disputed"
    AUTO_COMPLETED = "auto_completed"