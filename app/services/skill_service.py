from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.models.user import User
from app.repositories.skill_repository import SkillRepository
from app.schemas.skill_schema import (
    SkillCreate,
    SkillUpdate
)


class SkillService:

    def __init__(self):
        self.skill_repository = SkillRepository()

    def create_skill(
        self,
        db: Session,
        current_user: User,
        skill_data: SkillCreate
    ):

        skill = Skill(
            user_id=current_user.id,
            skill_name=skill_data.skill_name,
            proficiency=skill_data.proficiency
        )

        return self.skill_repository.create(
            db,
            skill
        )

    def get_my_skills(
        self,
        db: Session,
        current_user: User
    ):

        return self.skill_repository.get_all_by_user_id(
            db,
            current_user.id
        )

    def update_skill(
        self,
        db: Session,
        current_user: User,
        skill_id: int,
        skill_data: SkillUpdate
    ):

        skill = self.skill_repository.get_by_id(
            db,
            skill_id,
            current_user.id
        )

        if not skill:
            raise ValueError("Skill not found")

        update_data = skill_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(skill, key, value)

        return self.skill_repository.update(
            db,
            skill
        )

    def delete_skill(
        self,
        db: Session,
        current_user: User,
        skill_id: int
    ):

        skill = self.skill_repository.get_by_id(
            db,
            skill_id,
            current_user.id
        )

        if not skill:
            raise ValueError("Skill not found")

        self.skill_repository.delete(
            db,
            skill
        )

        return {
            "message": "Skill deleted successfully"
        }