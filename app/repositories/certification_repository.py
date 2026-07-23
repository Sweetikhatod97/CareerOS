from sqlalchemy.orm import Session

from app.models.certification import Certification


class CertificationRepository:

    def create(
        self,
        db: Session,
        certification: Certification
    ):

        db.add(certification)
        db.commit()
        db.refresh(certification)

        return certification

    def get_all_by_user_id(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Certification)
            .filter(Certification.user_id == user_id)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        certification_id: int,
        user_id: int
    ):

        return (
            db.query(Certification)
            .filter(
                Certification.id == certification_id,
                Certification.user_id == user_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        certification: Certification
    ):

        db.commit()
        db.refresh(certification)

        return certification

    def delete(
        self,
        db: Session,
        certification: Certification
    ):

        db.delete(certification)
        db.commit()