from uuid import UUID
from app.db.client import supabase
from app.schemas.user import UserRead
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
        .single()
        .execute()  
    )

    if response.data:
        return UserRead(**response.data)

    # user doesn't exist yet, make it 
    new_user = {
        "id": str(user_id),
        "display_name": _generate_display_name(),
        "anonymous_alias": _generate_anonymous_alias(),
    }

    insert_response = {
        supabase
        .table("users")
        .insert(new_user)
        .single()
        .execute()
    }

    return UserRead(**insert_response.data)