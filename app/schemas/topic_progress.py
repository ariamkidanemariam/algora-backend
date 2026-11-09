
from uuid import UUID
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


MasteryStatus = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "MASTERED",
]


class TopicProgressRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    topic_id: UUID
    problems_solved: int
    mastery_percentage: float = Field(ge=0, le=100)
    mastery_status: MasteryStatus
    updated_at: datetime