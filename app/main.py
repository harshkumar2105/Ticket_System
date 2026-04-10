from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user, ticket, admin

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Ticket Management System API is running"}

app.include_router(user.router, prefix="/auth")
app.include_router(ticket.router, prefix="/tickets")
app.include_router(admin.router, prefix="/admin")