from uuid import UUID

from pydantic import BaseModel, ConfigDict

class GitHubConnectionBase(BaseModel):
    name: str
    slug: str
    description: str | None = None
    order: int
    
class GitHubConnectionCreate(GitHubConnectionBase):
    pass

class GitHubConnectionUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    order: int | None = None

class GitHubConnectionRead(GitHubConnectionBase):
    model_config = ConfigDict(from_attributes=True)

    id: UUID