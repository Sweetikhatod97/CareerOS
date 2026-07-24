from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.resume_schema import ResumeResponse
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)

resume_service = ResumeService()


@router.get("", response_model=ResumeResponse)
def get_resume(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return resume_service.get_resume(
        db,
        current_user
    )