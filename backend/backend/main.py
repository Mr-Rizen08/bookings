from fastapi import FastAPI

from backend.api import v1_router

app = FastAPI(
    title="Booking API",
    version="0.0.1",
)

@app.get("/health")
async def get_health():
    return {"status": "ok"}


app.include_router(v1_router)
