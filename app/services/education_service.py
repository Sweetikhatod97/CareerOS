from sqlalchemy.orm import Session

from app.models.education import Education
from app.models.user import User
from app.repositories.education_repository import EducationRepository
from app.schemas.education_schema import (
    EducationCreate,
    EducationUpdate
)


class EducationService:

    def __init__(self):
        self.education_repository = EducationRepository()

    def create_education(
        self,
        db: Session,
        current_user: User,
        education_data: EducationCreate
    ):

        education = Education(
            user_id=current_user.id,
            college_name=education_data.college_name,
            degree=education_data.degree,
            field_of_study=education_data.field_of_study,
            start_year=education_data.start_year,
            end_year=education_data.end_year,
            cgpa=education_data.cgpa,
            description=education_data.description
        )

        return self.education_repository.create(
            db,
            education
        )

    def get_my_educations(
        self,
        db: Session,
        current_user: User
    ):

        return self.education_repository.get_all_by_user_id(
            db,
            current_user.id
        )

    def update_education(
        self,
        db: Session,
        current_user: User,
        education_id: int,
        education_data: EducationUpdate
    ):

        education = self.education_repository.get_by_id(
            db,
            education_id,
            current_user.id
        )

        if not education:
            raise ValueError("Education record not found")

        update_data = education_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(education, key, value)

        return self.education_repository.update(
            db,
            education
        )

    def delete_education(
        self,
        db: Session,
        current_user: User,
        education_id: int
    ):

        education = self.education_repository.get_by_id(
            db,
            education_id,
            current_user.id
        )

        if not education:
            raise ValueError("Education record not found")

        self.education_repository.delete(
            db,
            education
        )

        return {
            "message": "Education deleted successfully"
        }