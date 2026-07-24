from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.profile_repository import ProfileRepository
from app.repositories.education_repository import EducationRepository
from app.repositories.skill_repository import SkillRepository
from app.repositories.experience_repository import ExperienceRepository
from app.repositories.project_repository import ProjectRepository
from app.repositories.certification_repository import CertificationRepository


class ResumeService:

    def __init__(self):
        self.profile_repository = ProfileRepository()
        self.education_repository = EducationRepository()
        self.skill_repository = SkillRepository()
        self.experience_repository = ExperienceRepository()
        self.project_repository = ProjectRepository()
        self.certification_repository = CertificationRepository()

    def get_resume(
        self,
        db: Session,
        current_user: User
    ):

        return {
            "profile": self.profile_repository.get_by_user_id(
                db,
                current_user.id
            ),
            "education": self.education_repository.get_all_by_user_id(
                db,
                current_user.id
            ),
            "skills": self.skill_repository.get_all_by_user_id(
                db,
                current_user.id
            ),
            "experience": self.experience_repository.get_all_by_user_id(
                db,
                current_user.id
            ),
            "projects": self.project_repository.get_all_by_user_id(
                db,
                current_user.id
            ),
            "certifications": self.certification_repository.get_all_by_user_id(
                db,
                current_user.id
            )
        }