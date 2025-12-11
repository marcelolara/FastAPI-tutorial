from sqlmodel import SQLModel, Field
from typing import Optional

# Shared properties
class UserBase(SQLModel):
    email: str = Field(unique=True, index=True)
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str