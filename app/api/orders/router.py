from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.deps import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.api.orders.service import create_order, get_order


router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=OrderResponse)
async def create_order_api(
    payload: OrderCreate, 
    db: AsyncSession=Depends(get_db)
    ):
    order = await create_order(db, payload)
    
    return order


@router.get("/{order_id}", response_model=OrderResponse )
async def get_order_api(
    order_id: str,
    db: AsyncSession=Depends(get_db)
    ):
    order = await get_order(db, order_id)
    
    if not order:
        raise HTTPException(404, "order not found")
    return order