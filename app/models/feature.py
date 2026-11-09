from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from app.models.feature_attempt import FeatureAttempt
    from app.models.topic import Topic


class Feature(Base):
    
    __tablename__ = "features"

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

    topic_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("topics.id", ondelete="RESTRICT"), index=True
    )
    slug: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    brief: Mapped[str] = mapped_column(Text)  # the story, markdown

    # Plain-language rules shown to the learner: ["Up to 10 suggestions", ...]
    acceptance_rules: Mapped[list[str]] = mapped_column(JSONB, default=list)
    # e.g. {"lookup_p95_ms": 50}
    performance_limits: Mapped[dict[str, Any]] = mapped_column(JSONB, default=dict)
    # Where the runner finds the private test suite. Not exposed to learners.
    hidden_suite_ref: Mapped[str] = mapped_column(String(500))

    note_questions: Mapped[list[str]] = mapped_column(JSONB, default=list)
    example_note: Mapped[str] = mapped_column(Text, default="")  # shown after completion

    position: Mapped[int] = mapped_column(Integer, default=0)

    topic: Mapped[Topic] = relationship(back_populates="features")
    attempts: Mapped[list[FeatureAttempt]] = relationship(back_populates="feature")

    def __repr__(self) -> str:
        return f"<Feature {self.slug}>"
