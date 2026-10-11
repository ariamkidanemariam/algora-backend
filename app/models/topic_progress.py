import uuid
from datetime import datetime
from sqlalchemy import Integer, Float, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class TopicProgress(Base):
    __tablename__ = "topic_progress"
    __table_args__ = (UniqueConstraint("user_id", "topic_id", name="uq_user_topic_progress"),)
   
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    topic_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    problems_solved: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    mastery_percentage: Mapped[float] = mapped_column(Float, default=0, nullable=False)
    mastery_status: Mapped[str] = mapped_column(String(30), default="NOT_STARTED", nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
   
    user = relationship("User", back_populates="topic_progress")
    topic = relationship("Topic", back_populates="progress")
