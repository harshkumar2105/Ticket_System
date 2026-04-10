from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Ticket
from app.schemas import TicketCreate
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/")
def create_ticket(data: TicketCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ticket = Ticket(**data.dict(), created_by=user.id)
    db.add(ticket)
    db.commit()
    return ticket


@router.get("/")
def list_tickets(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Ticket).filter(Ticket.created_by == user.id).all()


@router.get("/{ticket_id}")
def get_ticket(ticket_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


@router.delete("/{ticket_id}")
def delete_ticket(ticket_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    db.delete(ticket)
    db.commit()
    return {"msg": "Deleted"}
