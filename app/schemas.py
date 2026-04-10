from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    category: str


class TicketUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
