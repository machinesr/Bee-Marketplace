from fastapi import FastAPI
from app.api.orders import router as orders_router

app = FastAPI(title="Bee Marketplace API")

app.include_router(orders_router, prefix="/api/v1")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Bee Marketplace Backend is running"}
