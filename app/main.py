from fastapi import FastAPI

from app.api.v1.home import router
from app.api.v1.auth import router as auth_router
from app.api.v1.profile import router as profile_router
from app.core.config import settings
from app.api.v1.education import router as education_router
from app.api.v1.skill import router as skill_router
from app.api.v1.experience import router as experience_router
from app.api.v1.project import router as project_router

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(router)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(education_router)
app.include_router(skill_router)
app.include_router(experience_router)
app.include_router(project_router)
