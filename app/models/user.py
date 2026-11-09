from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, DateTime, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from app.models.feature_attempt import FeatureAttempt
    from app.models.submission import Submission


class User(Base):
    __tablename__ = "users"

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

    username: Mapped[str] = mapped_column(String(39), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(320), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))  # never return in API
    email_verified_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    preferred_language: Mapped[str | None] = mapped_column(String(32))

    github_user_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    github_username: Mapped[str | None] = mapped_column(String(39))
    github_token_encrypted: Mapped[str | None] = mapped_column(Text)  # never return in API

    shop_repo_id: Mapped[int | None] = mapped_column(BigInteger, unique=True)
    shop_repo_full_name: Mapped[str | None] = mapped_column(String(140))
    shop_template_version: Mapped[str | None] = mapped_column(String(32))

    submissions: Mapped[list[Submission]] = relationship(
        back_populates="user", cascade="all, delete-orphan", passive_deletes=True
    )
    feature_attempts: Mapped[list[FeatureAttempt]] = relationship(
        back_populates="user", cascade="all, delete-orphan", passive_deletes=True
    )

    def __repr__(self) -> str:
        return f"<User {self.username}>"
