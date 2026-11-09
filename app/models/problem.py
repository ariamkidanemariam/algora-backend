from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from app.models.enums import Difficulty, pg_enum

if TYPE_CHECKING:
    from app.models.submission import Submission
    from app.models.topic import Topic


class Problem(Base):
    __tablename__ = "problems"

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
    description: Mapped[str] = mapped_column(Text)
    difficulty: Mapped[Difficulty] = mapped_column(pg_enum(Difficulty, "difficulty"))

    # Shown to the learner: [{"input": ..., "output": ..., "explanation": ...}]
    examples: Mapped[list[dict[str, Any]]] = mapped_column(JSONB, default=list)
    # NEVER return in API responses: [{"input": ..., "output": ...}]
    hidden_tests: Mapped[list[dict[str, Any]]] = mapped_column(JSONB, default=list)
    # Starter code per language: {"PYTHON": "...", "JAVASCRIPT": "..."}
    starter_code: Mapped[dict[str, str]] = mapped_column(JSONB, default=dict)

    time_limit_ms: Mapped[int] = mapped_column(Integer, default=2000)
    memory_limit_mb: Mapped[int] = mapped_column(Integer, default=256)
    position: Mapped[int] = mapped_column(Integer, default=0)

    topic: Mapped[Topic] = relationship(back_populates="problems")
    submissions: Mapped[list[Submission]] = relationship(back_populates="problem")

    def __repr__(self) -> str:
        return f"<Problem {self.slug}>"
