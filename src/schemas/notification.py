from typing import Dict, List

from pydantic import BaseModel, Field


class NotificationBase(BaseModel):
    title: str = Field(..., max_length=50)
    body: str = Field(None, max_length=200)


class NotificationIn(NotificationBase):
    uids: List[str] = Field(..., min_items=1)

class ProjectNotification(NotificationBase):
    projectid: int

class Notification(NotificationBase):
    tokens: List[str]
    data: Dict = Field(None)

class NotificationReport(NotificationBase):
    succeded: List[str] = Field(..., min_items=0)
    failed: List[str] = Field(..., min_items=0)