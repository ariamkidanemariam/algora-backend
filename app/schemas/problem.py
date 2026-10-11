
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ProblemBase(BaseModel):
    title: str
    slug: str
    description: str
    difficulty: str
    constraints: str | None = None
    explanation: str | None = None


class ProblemCreate(ProblemBase):
    topic_id: UUID


class ProblemUpdate(BaseModel):
    title: str | None = None
    slug: str | None = None
    description: str | None = None
    difficulty: str | None = None
    constraints: str | None = None
    explanation: str | None = None
    topic_id: UUID | None = None


class ProblemRead(ProblemBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    topic_id: UUID