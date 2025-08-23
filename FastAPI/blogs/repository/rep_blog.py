from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models
from .. import schema

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs 


def create(request: schema.BlogBase, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog Deleted'


def update(id: int, request: schema.BlogBase, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    blog.update({'title': 'Updated Title'}, synchronize_session=False)
    db.commit()
    return "Updated The Blog"


def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The blog with ID {id} is not available')
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f"Blog with ID {id} not available"}
    return blog
