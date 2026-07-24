from pydantic import BaseModel

from app.schemas.profile_schema import ProfileResponse
from app.schemas.education_schema import EducationResponse
from app.schemas.skill_schema import SkillResponse
from app.schemas.experience_schema import ExperienceResponse
from app.schemas.project_schema import ProjectResponse
from app.schemas.certification_schema import CertificationResponse


class ResumeResponse(BaseModel):
    profile: ProfileResponse | None
    education: list[EducationResponse]
    skills: list[SkillResponse]
    experience: list[ExperienceResponse]
    projects: list[ProjectResponse]
    certifications: list[CertificationResponse]