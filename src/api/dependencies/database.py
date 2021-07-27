from src.database.config import SessionLocal

# Dependency
def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()