from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, auth

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# Initialize FastAPI
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/register/", response_model=schemas.UserCreate)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = auth.hash_password(user.password)
    new_user = models.User(username=user.username, email=user.email, password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
