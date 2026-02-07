from fastapi import Depends
from app.services.user_service import get_or_create_user
from app.schemas.user import UserRead
from app.dependencies.auth import get_current_user_id

def get_current_user_details(
        user_id = Depends(get_current_user_id)
) -> UserRead:
    return get_or_create_user(user_id)  