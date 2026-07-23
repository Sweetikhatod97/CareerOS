from sqlalchemy.orm import Session

from app.models.experience import Experience
from app.models.user import User
from app.repositories.experience_repository import ExperienceRepository
from app.schemas.experience_schema import (
    ExperienceCreate,
    ExperienceUpdate
)


class ExperienceService:

    def __init__(self):
        self.experience_repository = ExperienceRepository()

    def create_experience(
        self,
        db: Session,
        current_user: User,
        experience_data: ExperienceCreate
    ):

        experience = Experience(
            user_id=current_user.id,
            company_name=experience_data.company_name,
            job_title=experience_data.job_title,
            employment_type=experience_data.employment_type,
            location=experience_data.location,
            start_date=experience_data.start_date,
            end_date=experience_data.end_date,
            currently_working=experience_data.currently_working,
            description=experience_data.description
        )

        return self.experience_repository.create(
            db,
            experience
        )

    def get_my_experiences(
        self,
        db: Session,
        current_user: User
    ):

        return self.experience_repository.get_all_by_user_id(
            db,
            current_user.id
        )

    def update_experience(
        self,
        db: Session,
        current_user: User,
        experience_id: int,
        experience_data: ExperienceUpdate
    ):

        experience = self.experience_repository.get_by_id(
            db,
            experience_id,
            current_user.id
        )

        if not experience:
            raise ValueError("Experience not found")

        update_data = experience_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(experience, key, value)

        return self.experience_repository.update(
            db,
            experience
        )

    def delete_experience(
        self,
        db: Session,
        current_user: User,
        experience_id: int
    ):

        experience = self.experience_repository.get_by_id(
            db,
            experience_id,
            current_user.id
        )

        if not experience:
            raise ValueError("Experience not found")

        self.experience_repository.delete(
            db,
            experience
        )

        return {
            "message": "Experience deleted successfully"
        }