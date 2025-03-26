from fastapi import FastAPI
from database import init_db, reset_db
from routers import todo, user

app = FastAPI()

# initialize database tables
@app.on_event("startup")
def on_startup():
    # reset_db()
    init_db()

# include routers
app.include_router(user.router)
app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Welcome to Todo App"}