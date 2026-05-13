from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    age: int
    city: str


class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: str
