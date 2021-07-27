from src.api.routes.common import succesfulResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.api.dependencies.database import getDB
from src.database.config import engine
from src.database import crud
from src.api.errors.ApiError import ApiError
import src.api.errors.messages as errMsg
router = APIRouter()


@router.get("/status")
def getStatus(db: Session = Depends(getDB)):
  try:
    crud.getStatus(db)
  except Exception as e:
    raise ApiError.serverError(errMsg.DATABASE_CONNECTION_ERROR)

  return succesfulResponse(200, None)
