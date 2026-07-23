from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.user import User
from app.repositories.project_repository import ProjectRepository
from app.schemas.project_schema import (
    ProjectCreate,
    ProjectUpdate
)


class ProjectService:

    def __init__(self):
        self.project_repository = ProjectRepository()

    def create_project(
        self,
        db: Session,
        current_user: User,
        project_data: ProjectCreate
    ):

        project = Project(
            user_id=current_user.id,
            project_title=project_data.project_title,
            description=project_data.description,
            technologies=project_data.technologies,
            github_url=project_data.github_url,
            live_url=project_data.live_url,
            start_date=project_data.start_date,
            end_date=project_data.end_date,
            currently_working=project_data.currently_working
        )

        return self.project_repository.create(
            db,
            project
        )

    def get_my_projects(
        self,
        db: Session,
        current_user: User
    ):

        return self.project_repository.get_all_by_user_id(
            db,
            current_user.id
        )

    def update_project(
        self,
        db: Session,
        current_user: User,
        project_id: int,
        project_data: ProjectUpdate
    ):

        project = self.project_repository.get_by_id(
            db,
            project_id,
            current_user.id
        )

        if not project:
            raise ValueError("Project not found")

        update_data = project_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(project, key, value)

        return self.project_repository.update(
            db,
            project
        )

    def delete_project(
        self,
        db: Session,
        current_user: User,
        project_id: int
    ):

        project = self.project_repository.get_by_id(
            db,
            project_id,
            current_user.id
        )

        if not project:
            raise ValueError("Project not found")

        self.project_repository.delete(
            db,
            project
        )

        return {
            "message": "Project deleted successfully"
        }