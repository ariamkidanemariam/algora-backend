from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import AttemptStatus, pg_enum

if TYPE_CHECKING:
    from app.models.check import Check
    from app.models.feature import Feature
    from app.models.user import User


class FeatureAttempt(Base):
    __tablename__ = "feature_attempts"
    __table_args__ = (
        UniqueConstraint("user_id", "feature_id", name="uq_attempt_user_feature"),
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
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True
    )
    feature_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("features.id", ondelete="RESTRICT"), index=True
    )
    status: Mapped[AttemptStatus] = mapped_column(
        pg_enum(AttemptStatus, "attempt_status"), default=AttemptStatus.IN_PROGRESS
    )
    passing_commit_sha: Mapped[str | None] = mapped_column(String(40))

    note_path: Mapped[str | None] = mapped_column(String(255))  # e.g. DESIGN.md
    note_commit_sha: Mapped[str | None] = mapped_column(String(40))

    tests_passed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    user: Mapped[User] = relationship(back_populates="feature_attempts")
    feature: Mapped[Feature] = relationship(back_populates="attempts")
    checks: Mapped[list[Check]] = relationship(
        back_populates="attempt",
        cascade="all, delete-orphan",
        passive_deletes=True,
        order_by="Check.created_at.desc()",
    )

    def __repr__(self) -> str:
        return f"<FeatureAttempt {self.id} {self.status}>"
