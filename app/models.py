from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .db import Base, engine, SessionLocal
from sqlalchemy.orm import relationship
# Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)






class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="Cascade"))
    user = relationship("User")
#user_id oluşturmuyor
Base.metadata.create_all(bind=engine)