from datetime import date

from pydantic import BaseModel, ConfigDict


class ExperienceBase(BaseModel):
    company_name: str
    job_title: str
    employment_type: str
    location: str
    start_date: date
    end_date: date | None = None
    currently_working: bool = False
    description: str | None = None


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceUpdate(BaseModel):
    company_name: str | None = None
    job_title: str | None = None
    employment_type: str | None = None
    location: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    currently_working: bool | None = None
    description: str | None = None


class ExperienceResponse(ExperienceBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )