
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from app.models.project_feature import ProjectFeatureStatus


class ProjectFeatureBase(BaseModel):
    title: str
    description: str | None = None
    dsa_topic_id: UUID | None = None


class ProjectFeatureCreate(ProjectFeatureBase):
    project_id: UUID


class ProjectFeatureUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    dsa_topic_id: UUID | None = None
    status: ProjectFeatureStatus | None = None


class ProjectFeatureRead(ProjectFeatureBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    status: ProjectFeatureStatus