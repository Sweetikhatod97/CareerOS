from fastapi import FastAPI

from app.api.v1.home import router
from app.api.v1.auth import router as auth_router
from app.api.v1.profile import router as profile_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(router)
app.include_router(auth_router)
app.include_router(profile_router)