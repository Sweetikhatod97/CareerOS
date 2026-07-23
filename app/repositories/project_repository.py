from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:

    def create(
        self,
        db: Session,
        project: Project
    ):

        db.add(project)
        db.commit()
        db.refresh(project)

        return project

    def get_all_by_user_id(
        self,
        db: Session,
        user_id: int
    ):

        return (
            db.query(Project)
            .filter(Project.user_id == user_id)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        project_id: int,
        user_id: int
    ):

        return (
            db.query(Project)
            .filter(
                Project.id == project_id,
                Project.user_id == user_id
            )
            .first()
        )

    def update(
        self,
        db: Session,
        project: Project
    ):

        db.commit()
        db.refresh(project)

        return project

    def delete(
        self,
        db: Session,
        project: Project
    ):

        db.delete(project)
        db.commit()