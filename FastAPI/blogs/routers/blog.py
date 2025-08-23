from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schema, models
from typing import List, Annotated
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import rep_blog
from ..oauth2 import get_current_user


router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get('/', response_model=List[schema.ShowBlog])
def all(current_user: Annotated[schema.User, Depends(get_current_user)], db: Session = Depends(get_db)):
    return rep_blog.get_all(db)

# adding a blog to our db table that we created
@router.post('/', response_model=schema.Blog, status_code=status.HTTP_201_CREATED)
def create(current_user: Annotated[schema.User, Depends(get_current_user)], request: schema.BlogBase, db: Session = Depends(get_db)):
    return rep_blog.create(request, db)


# using this method to delete a blog from the db
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(current_user: Annotated[schema.User, Depends(get_current_user)], id: int, db: Session = Depends(get_db)):
   return rep_blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(current_user: Annotated[schema.User, Depends(get_current_user)], id: int,request: schema.Blog, db: Session = Depends(get_db)):
    return rep_blog.update(id, request, db)



# getting a specific blog using the id, and log an error if the id dosent exist using "response" or "raise"
# we set response_model so that we choose to not dislay the id in the response, when we get a single blog
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowBlog)
def show(current_user: Annotated[schema.User, Depends(get_current_user)], id: int, db: Session = Depends(get_db)):
    return rep_blog.show(id, db)