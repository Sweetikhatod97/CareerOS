from sqlalchemy.orm import Session

from app.models.skill import Skill


class SkillRepository:

    def create(
        self,
        db: Session,
        skill: Skill
    ):

        db.add(skill)
        db.commit()
        db.refresh(skill)

        return skill

    def get_all_by_user_id(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Skill)
            .filter(Skill.user_id == user_id)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        skill_id: int,
        user_id: int
    ):

        return (
            db.query(Skill)
            .filter(
                Skill.id == skill_id,
                Skill.user_id == user_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        skill: Skill
    ):

        db.commit()
        db.refresh(skill)

        return skill

    def delete(
        self,
        db: Session,
        skill: Skill
    ):

        db.delete(skill)
        db.commit()