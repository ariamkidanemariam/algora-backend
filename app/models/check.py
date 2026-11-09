from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import DateTime, ForeignKey, Index, String, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from app.models.enums import CheckStatus, pg_enum

if TYPE_CHECKING:
    from app.models.feature_attempt import FeatureAttempt


class Check(Base):
    __tablename__ = "checks"
    __table_args__ = (
        Index("ix_checks_attempt_created", "attempt_id", "created_at"),
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

    attempt_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("feature_attempts.id", ondelete="CASCADE")
    )
    commit_sha: Mapped[str] = mapped_column(String(40))
    status: Mapped[CheckStatus] = mapped_column(
        pg_enum(CheckStatus, "check_status"), default=CheckStatus.PENDING, index=True
    )
    results: Mapped[dict[str, Any] | None] = mapped_column(JSONB)

    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))

    attempt: Mapped[FeatureAttempt] = relationship(back_populates="checks")

    def __repr__(self) -> str:
        return f"<Check {self.commit_sha[:7]} {self.status}>"
