from sqlalchemy.orm import Session

from app.models.profile import Profile


class ProfileRepository:

    def create(
        self,
        db: Session,
        profile: Profile
    ):

        db.add(profile)
        db.commit()
        db.refresh(profile)

        return profile

    def get_by_user_id(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Profile)
            .filter(Profile.user_id == user_id)
            .first()
        )

    def update(
        self,
        db: Session,
        profile: Profile
    ):

        db.commit()
        db.refresh(profile)

        return profile