from pydantic.fields import Undefined
from src.api.routes.common import succesfulResponse
from fastapi import APIRouter, Depends
from src.schemas.notification import \
    (NotificationIn,
    Notification,
    ProjectNotification,
    NotificationReport)
from src.schemas.user import User
from src.schemas.suscription import Suscription
from src.services import notification as notificationsService
from sqlalchemy.orm import Session
from src.api.dependencies.database import getDB
from src.database import crud
from typing import List, Callable, Type

router = APIRouter()


@router.post("/", response_model=List[NotificationReport])
def sendNotifications(notifications: List[NotificationIn], db: Session = Depends(getDB)):

    reports : List[NotificationReport] = []
    for noti in notifications:
        users = crud.getUsers(db, noti.uids)
        if (len(users) < 1):
            continue

        tokens = list(map(lambda user: user.token, users))
        uids = set(map(lambda user: user.id, users))
        failedIDs = list(set(noti.uids) - uids)

        report = notificationsService.sendNotification(Notification(**noti.dict(), tokens=tokens))
        succededUsers = crud.getUsersByTokens(db, report.succeded)
        failedUsers =  crud.getUsersByTokens(db, report.failed)

        report.succeded = [user.id for user in succededUsers]
        report.failed = failedIDs + [user.id for user in failedUsers]

        reports.append(report)

    return succesfulResponse(201, list(reports))


@router.post("/projects", response_model=NotificationReport)
def sendProjectNotification(notification: ProjectNotification, db: Session = Depends(getDB)):
    report : NotificationReport = Undefined
    subscribers = crud.getProjectSubscribers(db, notification.projectid)
    if (len(subscribers) > 0):
        tokens = [subscriber.token for subscriber in subscribers]
        noti = Notification(
            **notification.dict(),
            tokens=tokens,
            data={'projectid' : notification.projectid})
        report = notificationsService.sendNotification(noti)

    return succesfulResponse(201, report)
