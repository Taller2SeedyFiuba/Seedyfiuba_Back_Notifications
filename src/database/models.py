from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .config import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    token = Column(String, primary_key=False, index=False)

    suscriptions = relationship("Suscription", back_populates='user')

class Suscription(Base):
    __tablename__ = "suscriptions"

    projectid = Column(Integer, primary_key=True, index=True)
    userid = Column(String, ForeignKey("users.id"), primary_key=True)

    user = relationship("User", back_populates='suscriptions')