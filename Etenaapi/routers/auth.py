# # routers/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.email == user_data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = models.User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
def login(creds: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(
        models.User.email == creds.email, 
        models.User.password == creds.password
    ).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user.user_id, "name": user.name}

# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from database import get_db
# from models.user import User  # Points directly to the file above
# from schemas import UserCreate, UserLogin

# router = APIRouter(prefix="/auth", tags=["Authentication"])

# @router.post("/register")
# def register(user_data: UserCreate, db: Session = Depends(get_db)):
#     # Check if user exists
#     if db.query(User).filter(User.email == user_data.email).first():
#         raise HTTPException(status_code=400, detail="Email already registered")
    
#     new_user = User(**user_data.dict())
#     db.add(new_user)
#     db.commit()
#     return {"message": "Registered successfully"}

# @router.post("/login")
# def login(creds: UserLogin, db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.email == creds.email, User.password == creds.password).first()
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return {"message": "Login successful", "user_id": user.user_id}