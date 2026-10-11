import uuid
from sqlalchemy import String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class ProblemTemplate(Base):
    __tablename__ = "problem_templates"
    __table_args__ = (UniqueConstraint("problem_id", "language", name="uq_problem_language"),)
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    problem_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("problems.id", ondelete="CASCADE"), nullable=False)
    language: Mapped[str] = mapped_column(String(50), nullable=False)
    starter_code: Mapped[str] = mapped_column(Text, nullable=False)
    
    problem = relationship("Problem", back_populates="templates")
