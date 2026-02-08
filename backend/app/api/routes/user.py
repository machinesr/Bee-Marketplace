from fastapi import Depends, APIRouter
from app.schemas.user import UserRead, UserUpdate
from app.dependencies.user import get_current_user_details
from app.services.user_service import update_user

router = APIRouter(
    prefix="/users",
)

@router.get("/me", response_model=UserRead)
def me(user: UserRead = Depends(get_current_user_details)):
    return user

@router.patch("/me", response_model = UserUpdate)
def update_me(
    updates: UserUpdate,
    user: UserRead = Depends(get_current_user_details)
    ):
    return update_user(user.id, updates)