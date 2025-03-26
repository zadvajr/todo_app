import uuid
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from pydantic import EmailStr
from uuid import UUID

class UserBase(SQLModel):
    name: str
    email: EmailStr

class User(UserBase, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    todos: list('Todo') = Relationship(back_populates="owner")

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: UUID

class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    owner_id: UUID = Field(foreign_key="user.id")

class Todo(TodoBase, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    owner: User = Relationship(back_populates='todos')

class TodoCreate(TodoBase):
    pass

class TodoRead(TodoBase):
    id: UUID
