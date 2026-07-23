from sqlalchemy.orm import Session

from app.models.education import Education


class EducationRepository:

    def create(
        self,
        db: Session,
        education: Education
    ):

        db.add(education)
        db.commit()
        db.refresh(education)

        return education

    def get_all_by_user_id(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Education)
            .filter(Education.user_id == user_id)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        education_id: int,
        user_id: int
    ):

        return (
            db.query(Education)
            .filter(
                Education.id == education_id,
                Education.user_id == user_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        education: Education
    ):

        db.commit()
        db.refresh(education)

        return education

    def delete(
        self,
        db: Session,
        education: Education
    ):

        db.delete(education)
        db.commit()