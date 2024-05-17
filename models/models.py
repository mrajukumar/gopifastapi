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

class UserRoleCreate(BaseModel):
    user_id: int
    role_id: int

class UserRoleResponse(BaseModel):
    user_id: int
    role_id: int


class UserRoleRequest(BaseModel):
    user_id: int
    role_id: int


class SkillCreate(BaseModel):    
    name: str

class SkillUpdate(BaseModel):
    name: str
    

class SkillOut(BaseModel):
    skill_id:int
    name: str


class ChannelCreate(BaseModel):    
    name: str

class ChannelUpdate(BaseModel):    
    name: str

class ChannelsOut(BaseModel):
    channel_id:int
    name: str


class QueueCreate(BaseModel):    
     name :str
     wrapup_time:int

class QueueUpdate(BaseModel):    
     name :str
     wrapup_time:int

class QueueOut(BaseModel):
    queue_id: int
    name: str
    wrapup_time: int

class AddAgentToTeamRequest(BaseModel):
    agent_id: int   
    team_id: int

class GetTeamsForAgentRequest(BaseModel):
    agent_id: int

class UpdateAgentTeamRequest(BaseModel):
    agent_id: int   
    new_team_id: int

class GetAllAgentsResponse(BaseModel):
     agent_id: int   
     team_id: int


class RoutingProfileChannelCreate(BaseModel):
    routing_profile_id: int
    channel_id: int
    max_concurrent_interactions: int
    cross_channel_concurrency: int

class RoutingProfileChannelResponseBody(BaseModel):
    routing_profile_id: int
    channel_id: int
    max_concurrent_interactions: int
    cross_channel_concurrency: int

class RoutingProfileChannelResponse(BaseModel):
    routing_profile_id: int
    channel_id: int
    max_concurrent_interactions: int
    cross_channel_concurrency: int
