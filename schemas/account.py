import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AccountCreate(BaseModel):
    user_id: str
    user_pw: str
    name: str
    phone: str | None = None
    email: str | None = None


class AccountLogin(BaseModel):
    user_id: str
    user_pw: str


class AccountResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: str
    name: str
    phone: str | None = None
    email: str | None = None
    created_at: datetime
