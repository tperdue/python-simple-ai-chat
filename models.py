from datetime import datetime
from typing import List, Literal
from pydantic import BaseModel, Field
from uuid import uuid4

class ChatMessage(BaseModel):
    """Represents a single chat message."""
    role: Literal["user", "assistant"]
    content: str
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class DB(BaseModel):
    """Represents the database structure."""
    messages: List[ChatMessage] = []

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }