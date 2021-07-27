from pydantic import BaseModel

class Suscription(BaseModel):
    userid: str
    projectid: int
