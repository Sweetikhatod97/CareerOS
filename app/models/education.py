from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base import Base


class Education(Base):
    __tablename__ = "educations"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    college_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    degree: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    field_of_study: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    start_year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    end_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    cgpa: Mapped[float | None] = mapped_column(
        Numeric(3, 2),
        nullable=True
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="educations"
    )