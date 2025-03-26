from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from models import UserCreate, UserRead