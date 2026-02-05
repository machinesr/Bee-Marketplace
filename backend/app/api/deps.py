from fastapi import Depends, HTTPException, Header
from app.db.client import supabase


def get_current_user(authorization: str = Header(...)):
    """
    Validates the Supabase JWT and returns the User ID.
    """
    try:
        token = authorization.split(" ")[1]

        user_response = supabase.auth.get_user(token)

        if not user_response.user:
            raise Exception("User not found")

        return user_response.user.id

    except Exception as e:
        print(f"Auth Error: {e}")
        raise HTTPException(status_code=401, detail="Invalid Authentication Token")
