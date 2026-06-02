import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PostCreate(BaseModel):
    board_id: uuid.UUID
    author_id: uuid.UUID
    title: str
    content: str


class PostResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    board_id: uuid.UUID
    author_id: uuid.UUID
    title: str
    content: str
    view_count: int
    like_count: int
    created_at: datetime
