from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.api.routes import listings
from app.api.routes import user

app = FastAPI(title="Bee Marketplace API")
security = HTTPBearer()

app.include_router(listings.router)
app.include_router(user.router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Bee Marketplace Backend is running"}
