from fastapi import FastAPI
from app.api.routes.orders import router as orders_router
from app.api.routes import listings

app = FastAPI(title="Bee Marketplace API")

app.include_router(orders_router, prefix="/api/v1")
app.include_router(listings.router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Bee Marketplace Backend is running"}
