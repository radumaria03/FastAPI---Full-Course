from fastapi import Depends, status, HTTPException, Response, APIRouter
from .. import schema, models
from ..database import get_db
from ..repository import rep_user
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post('/', response_model=schema.ShowUser)
def create_user(request: schema.User, db: Session =Depends(get_db)):
    return  rep_user.create_user(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schema.ShowUser)
def show_user(id, response: Response, db: Session=Depends(get_db)):
    return rep_user.show_user(id, response, db)