from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.project import ProjectStatus


class ProjectCreate(BaseModel):
    title: str
    description: str | None = None
    status: ProjectStatus | None = ProjectStatus.NOT_STARTED
    live_url: str | None = None


class ProjectRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    title: str
    description: str | None = None
    status: ProjectStatus | None = ProjectStatus.NOT_STARTED
    live_url: str | None = None
    created_at: datetime
    updated_at: datetime