from datetime import date

from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    project_title: str
    description: str
    technologies: str
    github_url: str | None = None
    live_url: str | None = None
    start_date: date
    end_date: date | None = None
    currently_working: bool = False


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    project_title: str | None = None
    description: str | None = None
    technologies: str | None = None
    github_url: str | None = None
    live_url: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    currently_working: bool | None = None


class ProjectResponse(ProjectBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )