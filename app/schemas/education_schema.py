from pydantic import BaseModel, ConfigDict


class EducationBase(BaseModel):
    college_name: str
    degree: str
    field_of_study: str
    start_year: int
    end_year: int | None = None
    cgpa: float | None = None
    description: str | None = None


class EducationCreate(EducationBase):
    pass


class EducationUpdate(BaseModel):
    college_name: str | None = None
    degree: str | None = None
    field_of_study: str | None = None
    start_year: int | None = None
    end_year: int | None = None
    cgpa: float | None = None
    description: str | None = None


class EducationResponse(EducationBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )