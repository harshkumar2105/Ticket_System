from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Ticket
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.get("/tickets")
def all_tickets(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.role != "admin":
        return {"error": "Not allowed"}
    return db.query(Ticket).all()


@router.get("/stats")
def stats(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.role != "admin":
        return {"error": "Not allowed"}

    total = db.query(Ticket).count()
    open_tickets = db.query(Ticket).filter(Ticket.status == "open").count()

    return {"total": total, "open": open_tickets}
