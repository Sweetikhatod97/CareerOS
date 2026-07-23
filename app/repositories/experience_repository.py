from sqlalchemy.orm import Session

from app.models.experience import Experience


class ExperienceRepository:

    def create(
        self,
        db: Session,
        experience: Experience
    ):

        db.add(experience)
        db.commit()
        db.refresh(experience)

        return experience

    def get_all_by_user_id(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Experience)
            .filter(Experience.user_id == user_id)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        experience_id: int,
        user_id: int
    ):

        return (
            db.query(Experience)
            .filter(
                Experience.id == experience_id,
                Experience.user_id == user_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        experience: Experience
    ):

        db.commit()
        db.refresh(experience)

        return experience

    def delete(
        self,
        db: Session,
        experience: Experience
    ):

        db.delete(experience)
        db.commit()