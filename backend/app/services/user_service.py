from uuid import UUID
from app.db.client import supabase
from app.schemas.user import UserRead, UserUpdate
import random


def _generate_display_name() -> str:
    return "New User"

def _generate_anonymous_alias() -> str:
    return f"anon-{random.randint(1000,9999)}"

def get_or_create_user(user_id: UUID) -> UserRead:
    
    # find existing user
    response = (
        supabase
        .table("users")
        .select("*")
        .eq("id", str(user_id))
        .limit(1)
        .execute()  
    )

    if response.data:
        return UserRead(**response.data[0])

    # user doesn't exist yet, make it 
    new_user = {
        "id": str(user_id),
        "display_name": _generate_display_name(),
        "anonymous_alias": _generate_anonymous_alias(),
    }

    insert_response = (
        supabase
        .table("users")
        .insert(new_user)
        .execute()
    )



    return UserRead(**insert_response.data[0])

def update_user(user_id : UUID, updates: UserUpdate) -> UserUpdate:

    payload = updates.model_dump(exclude_none = True)

    if not payload: 
        return get_or_create_user(user_id)

    response = ( 
        supabase
        .table("users")
        .update(payload)
        .eq("id", str(user_id))
        .execute()
    )

    if response.data:
        return UserUpdate(**response.data[0])