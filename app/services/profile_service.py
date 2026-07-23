from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.models.user import User
from app.repositories.profile_repository import ProfileRepository
from app.schemas.profile_schema import (
    ProfileCreate,
    ProfileUpdate
)


class ProfileService:

    def __init__(self):
        self.profile_repository = ProfileRepository()

    def create_profile(
        self,
        db: Session,
        current_user: User,
        profile_data: ProfileCreate
    ):

        existing_profile = self.profile_repository.get_by_user_id(
            db,
            current_user.id
        )

        if existing_profile:
            raise ValueError("Profile already exists")

        profile = Profile(
            user_id=current_user.id,
            phone=profile_data.phone,
            date_of_birth=profile_data.date_of_birth,
            gender=profile_data.gender,
            city=profile_data.city,
            state=profile_data.state,
            country=profile_data.country,
            linkedin_url=str(profile_data.linkedin_url) if profile_data.linkedin_url else None,
            github_url=str(profile_data.github_url) if profile_data.github_url else None,
            portfolio_url=str(profile_data.portfolio_url) if profile_data.portfolio_url else None,
            bio=profile_data.bio,
            profile_image=str(profile_data.profile_image) if profile_data.profile_image else None,
        )

        return self.profile_repository.create(
            db,
            profile
        )

    def get_my_profile(
        self,
        db: Session,
        current_user: User
    ):

        profile = self.profile_repository.get_by_user_id(
            db,
            current_user.id
        )

        if not profile:
            raise ValueError("Profile not found")

        return profile

    def update_profile(
        self,
        db: Session,
        current_user: User,
        profile_data: ProfileUpdate
    ):

        profile = self.profile_repository.get_by_user_id(
            db,
            current_user.id
        )

        if not profile:
            raise ValueError("Profile not found")

        update_data = profile_data.model_dump(exclude_unset=True)

        # Convert HttpUrl objects to strings before saving
        for key, value in update_data.items():
            if value is not None:
                value = str(value)
            setattr(profile, key, value)

        return self.profile_repository.update(
            db,
            profile
        )