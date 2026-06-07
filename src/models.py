from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    created_at: datetime = datetime.now()

class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int
    status: str = "active"
    created_at: datetime = datetime.now()
