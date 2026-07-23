from sqlalchemy.orm import Session

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserRegister


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, db: Session, user_data: UserRegister):

        existing_user = self.user_repository.get_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise ValueError("Email already registered")

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hash_password(user_data.password)
        )

        return self.user_repository.create(db, user)

    def login(self, db: Session, username: str, password: str):

        user = self.user_repository.get_by_email(
            db,
            username
        )

        if not user:
            raise ValueError("Invalid email or password")

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise ValueError("Invalid email or password")

        token = create_access_token(
            data={"sub": user.email}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }