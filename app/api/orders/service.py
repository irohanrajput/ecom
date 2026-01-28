from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse

async def create_order(db: AsyncSession, data: OrderCreate) -> Order:
    order = Order(
        user_id=data.user_id,
        total_amount=data.total_amout
    )
    
    db.add(order)
    
    await db.commit()
    await db.refresh(order)
    
    return order

async def get_order(db:AsyncSession, order_id: str) -> Order | None:
    result = await db.execute(
        select(Order).where(Order.id==order_id)
        )
    return result.scalar_one_or_none()