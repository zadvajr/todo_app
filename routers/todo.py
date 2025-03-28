from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import TodoCreate, TodoRead
from crud.todo import todo_crud
from uuid import UUID

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=TodoRead)
def create_todo_endpoint(todo: TodoCreate, db: Session = Depends(get_session)):
    return todo_crud.create_todo(db, todo)

@router.get("/{todo_id}", response_model=TodoRead)
def get_todo_endpoint(todo_id: UUID, db: Session = Depends(get_session)):
    todo = todo_crud.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    return todo

@router.get("/", response_model=list[TodoRead])
def list_todos_endpoints(db: Session = Depends(get_session)):
    return todo_crud.list_todos(db)

@router.put("/{todo_id}", response_model=TodoRead)
def update_todo_endpoint(todo_id: UUID, todo: TodoCreate, db: Session = Depends(get_session)):
    updated_todo = todo_crud.update_todo(db, todo_id, todo)
    if not updated_todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    return {"message": "Todo updated successfully!"}

@router.delete("/{todo_id}")
def delete_todo_endpoint(todo_id: UUID, db: Session = Depends(get_session)):
    if not todo_crud.delete_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found!")
    return {"message": "Todo deleted successfully"}

@router.get("/user/{user_id}", response_model=list[TodoRead])
def get_todos_for_user(user_id: UUID, db: Session = Depends(get_session)):
    todos = todo_crud.list_todos_by_user(db, user_id)
    if not todos:
        raise HTTPException(status_code=404, detail = "No Todos found for this user")
    return todos