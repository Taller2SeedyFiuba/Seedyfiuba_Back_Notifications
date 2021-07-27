from src.api.routes.common import succesfulResponse
from fastapi import APIRouter, Depends, Query
from src.schemas import user, suscription, search
from src.api.errors.ApiError import ApiError
from sqlalchemy.orm import Session
from src.api.dependencies.database import getDB
from src.database import crud
from src.api.errors import messages as errMsg
from typing import List

router = APIRouter()


@router.post("/", response_model=suscription.Suscription)
def createSuscription(suscription: suscription.Suscription, db: Session = Depends(getDB)):
  dbUser = crud.getUser(db, suscription.userid)
  if not dbUser:
    raise ApiError.badRequest(errMsg.USER_NOT_FOUND)
  result = crud.createSuscription(db, suscription)

  return succesfulResponse(201, result)

@router.get("/", response_model=List[suscription.Suscription])
def getProjectSubscribers(
    id: str=Query(None), 
    projectid: int=Query(None, gt=0), 
    limit: int=Query(10, gt=0), 
    page: int=Query(1, gt=0), 
    db: Session = Depends(getDB)):

  searchParams = search.Search(userid=id, projectid=projectid, limit=limit, page=page)
  subscribers = crud.searchSubscribers(db, searchParams)
  
  return succesfulResponse(200, list(subscribers))

@router.delete("/{id}/projects/{projectid}", response_model=suscription.Suscription)
def deleteProjectSubscriber(id: str, projectid: int, db: Session = Depends(getDB)):
  sus = suscription.Suscription(userid=id, projectid=projectid)
  exists = crud.suscriptionExists(db, sus)
  if not exists:
    raise ApiError.badRequest(errMsg.SUSCRIPTION_NOT_FOUND)

  deleted = crud.deleteSuscription(db, sus)
  
  return succesfulResponse(200, deleted)