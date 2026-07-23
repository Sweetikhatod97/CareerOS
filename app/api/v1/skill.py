from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.skill_schema import (
    SkillCreate,
    SkillUpdate,
    SkillResponse
)
from app.services.skill_service import SkillService

router = APIRouter(
    prefix="/skill",
    tags=["Skill"]
)

skill_service = SkillService()


@router.post("", response_model=SkillResponse)
def create_skill(
    skill_data: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return skill_service.create_skill(
        db,
        current_user,
        skill_data
    )


@router.get("", response_model=list[SkillResponse])
def get_my_skills(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return skill_service.get_my_skills(
        db,
        current_user
    )


@router.put("/{skill_id}", response_model=SkillResponse)
def update_skill(
    skill_id: int,
    skill_data: SkillUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return skill_service.update_skill(
            db,
            current_user,
            skill_id,
            skill_data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return skill_service.delete_skill(
            db,
            current_user,
            skill_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )