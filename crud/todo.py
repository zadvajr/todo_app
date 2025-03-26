from sqlmodel import Session, select
from fastapi import HTTPException
from models import Todo, TodoCreate
from uuid import UUID

class TodoCrud:
    @staticmethod
    def create_todo(db: Session, todo: TodoCreate):
        db_todo = Todo(**todo.model_dump())
        db.add(db_todo)
        return db_todo
    
    @staticmethod
    def get_todo(db: Session, todo_id: UUID):
        return db.get(Todo, todo_id)
    
    @staticmethod
    def list_todos(db: Session):
        return db.exec(select(Todo)).all()
    
    @staticmethod
    def update_todos(db: Session, todo_id: UUID, todo_data: TodoCreate):
        db_todo = db.get(Todo, todo_id)
        if not db_todo:
            raise HTTPException(status_code=400, detail="Todo with ID does not exist")
        for key, value in todo_data.model_dump().items():
            setattr(db_todo, key, value)
        return db_todo
    
    @staticmethod
    def delete_todo(db: Session, todo_id: UUID):
        todo = db.get(Todo, todo_id)
        if not todo:
            raise HTTPException(status_code=400, detail="Todo with ID does not exist")
        if todo:
            db.delete(todo)
            return True
        return False
    
    @staticmethod
    def list_todos_by_user(db: Session, todo_id: UUID):
        return db.exec(select(Todo).where(Todo.owner_id == user_id)).all()