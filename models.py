from sqlalchemy import Column, Integer, String, TIMESTAMP, Float
from database import Base
from sqlalchemy.sql import func



class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    amount = Column(Float)
    category = Column(String(200))
    created_on = Column(TIMESTAMP, server_default=func.now())
