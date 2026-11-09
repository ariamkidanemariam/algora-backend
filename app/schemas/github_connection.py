from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class GitHubConnectionBase(BaseModel):
    github_user_id: int
    github_username: str


class GitHubConnectionCreate(GitHubConnectionBase):
    access_token: str


class GitHubConnectionRead(GitHubConnectionBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    user_id: UUID
    connected_at: datetime


class GitHubConnectionUpdate(BaseModel):
    pass