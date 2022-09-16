from fastapi import FastAPI, Response, Path, Query,HTTPException,status, Depends
import uvicorn
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship





app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

models.Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]= None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float]= None
    brand: Optional[str]= None






@app.get("/")
async def root():
    return {"message": "Hello World"}


inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None, description="The Id of The Product You Would Like To See")):
    return inventory[item_id]

@app.get("/hello/{name}")
def hello(name):
    return f"Hi {name}"

@app.get("/get-by-name/{item_id}")
def get_item(*,item_id: int, name:str=None):
    for item_id in inventory:
        if inventory[item_id].name== name:
            return inventory[item_id]
    return {"Data": "Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item:Item):
    if item_id in inventory:
        return {"Errror":"Item Id Already Exists"}
    inventory[item_id]=item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item:UpdateItem):
    if item_id not in inventory:
        return {"Errror": "Item Id Does Not Exists"}
    if item.name != None:
        inventory[item_id].name =  item.name
    if item.price != None:
        inventory[item_id].price =  item.price
    if item.brand != None:
        inventory[item_id].brand =  item.brand

    return inventory[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        return {"Error": "Item Does Not Exist"}
    del inventory[item_id]
    return {"Message": "Item Deleted"}