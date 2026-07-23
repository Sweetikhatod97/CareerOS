from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.experience_schema import (
    ExperienceCreate,
    ExperienceUpdate,
    ExperienceResponse
)
from app.services.experience_service import ExperienceService

router = APIRouter(
    prefix="/experience",
    tags=["Experience"]
)

experience_service = ExperienceService()


@router.post("", response_model=ExperienceResponse)
def create_experience(
    experience_data: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return experience_service.create_experience(
        db,
        current_user,
        experience_data
    )


@router.get("", response_model=list[ExperienceResponse])
def get_my_experiences(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return experience_service.get_my_experiences(
        db,
        current_user
    )


@router.put("/{experience_id}", response_model=ExperienceResponse)
def update_experience(
    experience_id: int,
    experience_data: ExperienceUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return experience_service.update_experience(
            db,
            current_user,
            experience_id,
            experience_data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete("/{experience_id}")
def delete_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return experience_service.delete_experience(
            db,
            current_user,
            experience_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )