from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
import models
import schemas


import azure.functions as func

app = FastAPI()


@app.on_event("startup")
def startup():

    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:

        db.close()


@app.get("/")
def get_ready():
    return {"message": "Ready to use"}




@app.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    expenses = db.query(models.Expense).all()
    return {"code": 200, "message": "Expenses", "data": expenses}


@app.post("/add/expense")
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(
        name=expense.name, amount=expense.amount, category=expense.category
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return {"code": 200, "message": "Expense added", "data": db_expense}


@app.get("/expense/month/{month}/{year}")
def get_expense_by_month(month: int, year: int, db: Session = Depends(get_db)):
    expenses = (
        db.query(models.Expense)
        .filter(
            func.extract("month", models.Expense.created_on) == month,
            func.extract("year", models.Expense.created_on) == year,
        )
        .all()
    )
    return {"code": 200, "message": f"Expenses for {month}/{year}", "data": expenses}


@app.get("/totals/{salary}")
def get_total_expenses(salary: float, db: Session = Depends(get_db)):
    total = db.query(func.sum(models.Expense.amount)).scalar()
    if total is not None:
        total = float(total)
        remaining = salary - total
        return {
            "code": 200,
            "message": "Total expenses",
            "data": total,
            "remaining": remaining,
            "salary": salary,
        }
    return {"code": 200, "message": "Total expenses", "data": ""}
