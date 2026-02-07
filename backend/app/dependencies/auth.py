from fastapi import HTTPException, Header
import jwt
from jwt import InvalidTokenError
from app.core.config import settings

def get_current_user(authorization: str = Header(...)):
    
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header format",
        )

    token = authorization.removeprefix("Bearer ").strip()

    if not token:
        raise HTTPException(
            status_code = 401,
            detail = "missing auth token"
        )

    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated"
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail = "Invalid or expired auth token"
        )
    
    user_id = payload.get("sub")
    
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail = "Invalid token payload"
        )
    
    return user_id