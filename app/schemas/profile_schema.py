from datetime import date

from pydantic import BaseModel, ConfigDict, HttpUrl


class ProfileBase(BaseModel):
    phone: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None

    city: str | None = None
    state: str | None = None
    country: str | None = None

    linkedin_url: HttpUrl | None = None
    github_url: HttpUrl | None = None
    portfolio_url: HttpUrl | None = None

    bio: str | None = None
    profile_image: HttpUrl | None = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(ProfileBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)