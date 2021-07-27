from pydantic import BaseModel, Field

class Search(BaseModel):
    userid: str = Field(None)
    projectid: int = Field(None, gt=0)
    limit: int = Field(10, gt=0)
    page: int = Field(1, gt=0)

