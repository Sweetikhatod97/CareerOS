from sqlalchemy.orm import Session

from app.models.certification import Certification
from app.models.user import User
from app.repositories.certification_repository import CertificationRepository
from app.schemas.certification_schema import (
    CertificationCreate,
    CertificationUpdate
)


class CertificationService:

    def __init__(self):
        self.certification_repository = CertificationRepository()

    def create_certification(
        self,
        db: Session,
        current_user: User,
        certification_data: CertificationCreate
    ):

        certification = Certification(
            user_id=current_user.id,
            certificate_name=certification_data.certificate_name,
            issuing_organization=certification_data.issuing_organization,
            issue_date=certification_data.issue_date,
            expiry_date=certification_data.expiry_date,
            credential_id=certification_data.credential_id,
            credential_url=certification_data.credential_url
        )

        return self.certification_repository.create(
            db,
            certification
        )

    def get_my_certifications(
        self,
        db: Session,
        current_user: User
    ):

        return self.certification_repository.get_all_by_user_id(
            db,
            current_user.id
        )

    def update_certification(
        self,
        db: Session,
        current_user: User,
        certification_id: int,
        certification_data: CertificationUpdate
    ):

        certification = self.certification_repository.get_by_id(
            db,
            certification_id,
            current_user.id
        )

        if not certification:
            raise ValueError("Certification not found")

        update_data = certification_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(certification, key, value)

        return self.certification_repository.update(
            db,
            certification
        )

    def delete_certification(
        self,
        db: Session,
        current_user: User,
        certification_id: int
    ):

        certification = self.certification_repository.get_by_id(
            db,
            certification_id,
            current_user.id
        )

        if not certification:
            raise ValueError("Certification not found")

        self.certification_repository.delete(
            db,
            certification
        )

        return {
            "message": "Certification deleted successfully"
        }