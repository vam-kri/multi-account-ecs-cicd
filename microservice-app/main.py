from fastapi import FastAPI, HTTPException
from models import User
import uuid

app = FastAPI()
db = {}

@app.get("/")
def health_check():
    return {"message": "FastAPI User Microservice running"}

@app.post("/users")
def create_user(user: User):
    user_id = str(uuid.uuid4())
    db[user_id] = user
    return {"id": user_id, "user": user}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    if user_id not in db:
        raise HTTPException(status_code=404, detail="User not found")
    return db[user_id]
