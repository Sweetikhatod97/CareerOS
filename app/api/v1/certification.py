from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.certification_schema import (
    CertificationCreate,
    CertificationUpdate,
    CertificationResponse
)
from app.services.certification_service import CertificationService

router = APIRouter(
    prefix="/certification",
    tags=["Certification"]
)

certification_service = CertificationService()


@router.post("", response_model=CertificationResponse)
def create_certification(
    certification_data: CertificationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return certification_service.create_certification(
        db,
        current_user,
        certification_data
    )


@router.get("", response_model=list[CertificationResponse])
def get_my_certifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return certification_service.get_my_certifications(
        db,
        current_user
    )


@router.put("/{certification_id}", response_model=CertificationResponse)
def update_certification(
    certification_id: int,
    certification_data: CertificationUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return certification_service.update_certification(
            db,
            current_user,
            certification_id,
            certification_data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.delete("/{certification_id}")
def delete_certification(
    certification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return certification_service.delete_certification(
            db,
            current_user,
            certification_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )