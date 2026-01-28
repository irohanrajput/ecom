from fastapi import FastAPI
from app.api.orders.router import router as orders_router

app = FastAPI(title="ecom")

app.include_router(orders_router)

@app.get("/health")
def health_check():
    return {"status: ok"}