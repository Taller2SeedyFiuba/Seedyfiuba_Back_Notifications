from src.api.routes.common import succesfulResponse
from fastapi import APIRouter, Depends
from src.schemas import user
from src.api.errors.ApiError import ApiError
from sqlalchemy.orm import Session
from src.api.dependencies.database import getDB
from src.database import crud

router = APIRouter()


@router.put("/", response_model=user.User)
def createUser(user: user.User, db: Session = Depends(getDB)):
    dbUser = crud.getUser(db, user.id)
    if not dbUser:
        dbUser = crud.createUser(db, user)
    else:
        dbUser = crud.updateUser(db, user)
    return succesfulResponse(200, dbUser)

@router.delete("/{id}", response_model=user.UserOut)
def deleteUser(id: str, db: Session = Depends(getDB)):
    dbUser = crud.getUser(db, id)
    if not dbUser:
        raise ApiError.badRequest('user-not-exists')
    dbUser = crud.deleteUser(db, id)
    responseData = user.UserOut(**dbUser.dict())
    
    return succesfulResponse(200, responseData)