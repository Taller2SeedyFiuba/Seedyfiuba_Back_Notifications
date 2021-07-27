from fastapi import APIRouter

from src.api.routes import users, notifications, subscriptions, status

router = APIRouter()
router.include_router(users.router, tags=["users"], prefix="/users")
router.include_router(notifications.router, tags=["notifications"], prefix="/notifications")
router.include_router(subscriptions.router, tags=["subscriptions"], prefix="/subscribers")
router.include_router(status.router, tags=["status"])