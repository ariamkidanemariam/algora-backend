
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.submission import ProgrammingLanguage


class ProblemTemplateBase(BaseModel):
    language: ProgrammingLanguage
    starter_code: str


class ProblemTemplateCreate(ProblemTemplateBase):
    problem_id: UUID


class ProblemTemplateUpdate(BaseModel):
    language: ProgrammingLanguage | None = None
    starter_code: str | None = None


class ProblemTemplateRead(ProblemTemplateBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    problem_id: UUID