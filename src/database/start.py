from . import models
from src.database import models
from src.database.config import engine

def startDatabase():
    models.Base.metadata.create_all(bind=engine)
