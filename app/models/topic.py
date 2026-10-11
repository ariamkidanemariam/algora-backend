import uuid
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Topic(Base):
    __tablename__ = "topics"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    order: Mapped[int] = mapped_column(Integer, nullable=False)

    problems = relationship("Problem", back_populates="topic", cascade="all, delete-orphan")
    progress = relationship("TopicProgress", back_populates="topic", cascade="all, delete-orphan")
    features = relationship("ProjectFeature", back_populates="dsa_topic")
