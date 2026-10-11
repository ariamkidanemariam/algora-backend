import uuid
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, Float, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from enum import Enum
class SubmissionStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    ACCEPTED = "ACCEPTED"
    WRONG_ANSWER = "WRONG_ANSWER"
    RUNTIME_ERROR = "RUNTIME_ERROR"
    COMPILATION_ERROR = "COMPILATION_ERROR"
    TIME_LIMIT_EXCEEDED = "TIME_LIMIT_EXCEEDED"
    MEMORY_LIMIT_EXCEEDED = "MEMORY_LIMIT_EXCEEDED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
class ProgrammingLanguage(str, Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    DART = "dart"
    PYTHON3 = "python3"

class Submission(Base):
    __tablename__ = "submissions"
   
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problems.id", ondelete="CASCADE"), nullable=False)
    language: Mapped[ProgrammingLanguage] = mapped_column(SQLAlchemyEnum(ProgrammingLanguage), nullable=False)
    code: Mapped[str] = mapped_column(Text, nullable=False)
    status: Mapped[SubmissionStatus] = mapped_column(SQLAlchemyEnum(SubmissionStatus, name="submission_status", values_callable=lambda enum_cls: [ member.value for member in enum_cls],), nullable=False, default=SubmissionStatus.PENDING, nullable=False)
    runtime: Mapped[float | None] = mapped_column(Float)
    memory: Mapped[float | None] = mapped_column(Float)
    submitted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    
    user = relationship("User", back_populates="submissions")
    problem = relationship("Problem", back_populates="submissions")
