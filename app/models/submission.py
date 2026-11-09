from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import DateTime, Float, ForeignKey, Index, Integer, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from app.models.enums import Language, SubmissionStatus, pg_enum

if TYPE_CHECKING:
    from app.models.problem import Problem
    from app.models.user import User


class Submission(Base):
    __tablename__ = "submissions"
    __table_args__ = (
        Index("ix_submissions_user_problem", "user_id", "problem_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE")
    )
    problem_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("problems.id", ondelete="RESTRICT"), index=True
    )
    language: Mapped[Language] = mapped_column(pg_enum(Language, "language"))
    code: Mapped[str] = mapped_column(Text)

    status: Mapped[SubmissionStatus] = mapped_column(
        pg_enum(SubmissionStatus, "submission_status"),
        default=SubmissionStatus.PENDING,
        index=True,
    )
    runtime_ms: Mapped[int | None] = mapped_column(Integer)
    memory_mb: Mapped[float | None] = mapped_column(Float)
    result: Mapped[dict[str, Any] | None] = mapped_column(JSONB)

    judged_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    user: Mapped[User] = relationship(back_populates="submissions")
    problem: Mapped[Problem] = relationship(back_populates="submissions")

    def __repr__(self) -> str:
        return f"<Submission {self.id} {self.status}>"
