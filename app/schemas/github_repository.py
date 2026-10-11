
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class GitHubRepositoryBase(BaseModel):
    repository_name: str
    repository_url: str
    default_branch: str = "main"


class GitHubRepositoryCreate(GitHubRepositoryBase):
    project_id: UUID
    github_repo_id: int


class GitHubRepositoryUpdate(BaseModel):
    repository_name: str | None = None
    repository_url: str | None = None
    default_branch: str | None = None


class GitHubRepositoryRead(GitHubRepositoryBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    project_id: UUID
    github_repo_id: int