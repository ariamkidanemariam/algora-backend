
from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.submission import ProgrammingLanguage, SubmissionStatus


class SubmissionCreate(BaseModel):
    problem_id: UUID
    language: ProgrammingLanguage
    code: str


class SubmissionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    problem_id: UUID
    language: ProgrammingLanguage
    code: str
    status: SubmissionStatus
    runtime: float | None
    memory: float | None
    submitted_at: datetime