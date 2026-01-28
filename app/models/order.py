import uuid
from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.enums import OrderStatus



class Order(Base):
    __tablename__ = "orders"
    
    
    id:Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    
    user_id:Mapped[str] = mapped_column(
        String, 
        nullable=False,
    )
    
    status:Mapped[OrderStatus] = mapped_column(
        String,
        nullable=False,
        default=OrderStatus.CREATED,
    )
    
    total_amount:Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    
    created_at:Mapped[str] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    updated_at:Mapped[str] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
    