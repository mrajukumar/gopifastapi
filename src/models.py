from pydantic import BaseModel
from typing import Optional
import datetime

class UserCreate(BaseModel):
    userid: str
    password: str
    name: str
    email: str
    role_id: int
    extension: Optional[str] = None
    team_id: Optional[int] = None
    is_active: bool = True
    routing_profile_id: Optional[int] = None

class UserResponse(BaseModel):
    user_id: int
    userid: str
    password: str
    name: str
    email: str
    role_id: int
    extension: Optional[str] = None
    team_id: Optional[int] = None
    is_active: bool = True
    routing_profile_id: Optional[int] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime


class CreateRole(BaseModel):
    name: str


class RoleResponse(BaseModel):
    role_id: int
    name: str

class CreateRoutingProfile(BaseModel):
    name:str
    description:str

class RoutingProfileResponse(BaseModel):
    routing_profile_id: int
    name:str
    description:str

class TeamCreate(BaseModel):
    name:str
    description:str

class TeamUpdate(BaseModel):    
    name:str
    description:str

class TeamResponse(BaseModel):
    team_id: int
    name:str
    description:str