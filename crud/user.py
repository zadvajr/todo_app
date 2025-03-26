from sqlmodel import Session, select
from fastapi import HTTPException
from models import User, UserCreate
from uuid import UUID

class UserCrud:
    @staticmethod
    def create_user(db: Session, user: UserCreate):
        db_user = User(**user.model_dump())
        db.add(db_user)
        return db_user
    
    @staticmethod
    def get_user(db: Session, user_id: UUID):
        return db.get(User, user_id)
    
    @staticmethod
    def list_users(db: Session):
        return db.exec(select(User)).all()
    
    @staticmethod
    def delete_user(db: Session, user_id: UUID):
        user = db.get(User, user_id)
        if not user:
            raise HTTPException(status_code=400, detail="User with ID does not exist")
        if user:
            db.delete(user)
            return True
        return False

user_crud = UserCrud()