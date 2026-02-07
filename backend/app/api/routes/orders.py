from fastapi import APIRouter, HTTPException, Depends
from app.schemas.order import OrderCreate
from app.db.client import supabase
from app.dependencies.auth import get_current_user  

router = APIRouter()


@router.post("/orders")
def create_order(
    order: OrderCreate,
    user_id: str = Depends(get_current_user), 
):
    # 1. Convert UUIDs to strings
    listing_id_str = str(order.listing_id)

    # 2. Fetch Listing Data
    response = supabase.table("listings").select("*").eq("id", listing_id_str).execute()

    if not response.data:
        raise HTTPException(status_code=404, detail="Listing not found")

    listing = response.data[0]

    # 3. Validate Rules
    # Rule: "Inactive listings cannot be ordered"
    if not listing["is_active"]:
        raise HTTPException(status_code=400, detail="Listing is inactive")

    # Rule: "Stock cannot go negative"
    if listing["type"] == "digital_item" and listing["stock"] < 1:
        raise HTTPException(status_code=400, detail="Out of stock")

    # Rule: "Order cannot be self-dealing"
    seller_profile = (
        supabase.table("seller_profiles").select("user_id").eq("id", listing["seller_id"]).single().execute()
    )

    if seller_profile.data["user_id"] == user_id:
        raise HTTPException(status_code=400, detail="You cannot buy your own listing")

    # 4. Execute Atomic Transaction (RPC)
    try:
        rpc_params = {"p_buyer_id": user_id, "p_listing_id": listing_id_str, "p_seller_id": listing["seller_id"]}
        result = supabase.rpc("create_order_atomic", rpc_params).execute()
        return {"status": "success", "order_id": result.data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
