from logging import exception
from sqlalchemy.orm import Session

from src.database import models
from src.schemas.user import User
from src.schemas.suscription import Suscription
from src.schemas.search import Search
from typing import List, Union


def convertToPydantic(user : models.User) -> User:
    return User(**user.__dict__)

def getStatus(db: Session) -> None:
    db.execute('SELECT 1 + 1')

def getUser(db: Session, id : str) -> Union[User, None]:
    dbUser = db.query(models.User).filter(models.User.id == id).first()
    if not dbUser: return None
    return convertToPydantic(dbUser)

def getUsers(db: Session, ids: List[str]) -> List[User]:
    result = db.query(models.User).filter(models.User.id.in_(ids)).all()
    return [convertToPydantic(user) for user in result]

def getUsersByTokens(db: Session, tokens: List[str]) -> List[User]:
    result = db.query(models.User).filter(models.User.token.in_(tokens)).all()
    return [convertToPydantic(user) for user in result]

def createUser(db: Session, user: User) -> User:
    dbUser = models.User(**user.dict())
    db.add(dbUser)
    db.commit()
    db.refresh(dbUser)
    return convertToPydantic(dbUser)

def updateUser(db: Session, user: User) -> User:
    db.query(models.User).\
    filter(models.User.id == user.id).\
    update({'token' : user.token})
    db.commit()

    result = getUser(db, user.id)

    if not result:
        raise Exception('database-error')
    
    return result
    
def deleteUser(db: Session, id: str) -> User:
    dbUser = db.query(models.User).filter(models.User.id == id).one()
    db.delete(dbUser)
    db.commit()
    return convertToPydantic(dbUser)


def createSuscription(db: Session, suscription: Suscription) -> Suscription:
    
    dbSuscription = models.Suscription(**suscription.dict())
    db.add(dbSuscription)
    db.commit()
    db.refresh(dbSuscription)

    return Suscription(**dbSuscription.__dict__)

def suscriptionExists(db: Session, suscription: Suscription) -> bool:
    result = db.query(models.Suscription)\
        .filter(models.Suscription.userid == suscription.userid)\
        .filter(models.Suscription.projectid == suscription.projectid)\
        .first()
    print(result)
    return True if result else False

def searchSubscribers(db: Session, params : Search) -> List[Suscription]:

    query = db.query(models.Suscription)

    if (params.userid):
        query = query.filter(models.Suscription.userid == params.userid)
    if (params.projectid):
        query = query.filter(models.Suscription.projectid == params.projectid)
    
    result = query.limit(params.limit).offset((params.page - 1) * params.limit).all()

    return [Suscription(**sus.__dict__) for sus in result]
    

def getProjectSubscribers(db: Session, projectid: int) -> List[User]:

    suscriptions = db.query(models.Suscription).filter(models.Suscription.projectid == projectid).all()

    return [User(id=sus.userid, token=sus.user.token) for sus in suscriptions]

def deleteSuscription(db: Session, suscription: Suscription) -> Suscription:

    dbSus = db.query(models.Suscription)\
            .filter(models.Suscription.userid == suscription.userid)\
            .filter(models.Suscription.projectid == suscription.projectid)\
            .one()
    db.delete(dbSus)
    db.commit()

    return Suscription(**dbSus.__dict__)

