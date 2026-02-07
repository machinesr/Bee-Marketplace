from fastapi import Depends, APIRouter
from app.schemas.user import UserRead
from app.dependencies.user import get_current_user_details

router = APIRouter(
    prefix="/users",
)

@router.get("/me", response_model=UserRead)
def me(user: UserRead = Depends(get_current_user_details)):
    return user