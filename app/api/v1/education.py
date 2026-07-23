from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.education_schema import (
    EducationCreate,
    EducationUpdate,
    EducationResponse
)
from app.services.education_service import EducationService

router = APIRouter(
    prefix="/education",
    tags=["Education"]
)

education_service = EducationService()


@router.post("", response_model=EducationResponse)
def create_education(
    education_data: EducationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return education_service.create_education(
        db,
        current_user,
        education_data
    )


@router.get("", response_model=list[EducationResponse])
def get_my_educations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return education_service.get_my_educations(
        db,
        current_user
    )


@router.put("/{education_id}", response_model=EducationResponse)
def update_education(
    education_id: int,
    education_data: EducationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return education_service.update_education(
            db,
            current_user,
            education_id,
            education_data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete("/{education_id}")
def delete_education(
    education_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return education_service.delete_education(
            db,
            current_user,
            education_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )