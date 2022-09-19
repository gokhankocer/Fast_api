from fastapi import FastAPI, Response, Path, Query, HTTPException, status, Depends

from sqlalchemy.orm import sessionmaker, Session

from app.models import Post

from app.schemas import PostCreate
from app.db import get_db

app = FastAPI()

# Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"Data": "Welcome"}


@app.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}
