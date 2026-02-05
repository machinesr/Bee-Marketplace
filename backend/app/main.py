from fastapi import FastAPI
from app.api.orders import router as orders_router
<<<<<<< Updated upstream
=======
from app.api.routes import listings
>>>>>>> Stashed changes

app = FastAPI(title="Bee Marketplace API")

app.include_router(orders_router, prefix="/api/v1")
<<<<<<< Updated upstream
=======
app.include_router(listings.router)
>>>>>>> Stashed changes


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Bee Marketplace Backend is running"}
