from pydantic import BaseModel
from app.models.enums import OrderStatus


class OrderCreate(BaseModel):
    user_id: str
    total_amout: int
    
class OrderResponse(BaseModel):
    id: str
    user_id: str
    status: OrderStatus
    total_amount: int
    
    
    
    class Config:
        from_attributes = True