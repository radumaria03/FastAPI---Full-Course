from fastapi import APIRouter, Depends, HTTPException, status
from .. import schema, database, models
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..schema import Token
from fastapi.security import  OAuth2PasswordRequestForm
from .token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(
    tags=["Login"]
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="User not found")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Incorrect Password")
    
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}) #, expires_delta=access_token_expires
    
    return Token(access_token=access_token, token_type="bearer")
    