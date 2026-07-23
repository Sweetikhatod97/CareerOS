from pydantic import BaseModel, ConfigDict


class SkillBase(BaseModel):
    skill_name: str
    proficiency: str


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    skill_name: str | None = None
    proficiency: str | None = None


class SkillResponse(SkillBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )