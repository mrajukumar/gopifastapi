from fastapi import FastAPI, HTTPException
from typing import List
from models.models import UserCreate, UserResponse, CreateRole, RoleResponse, CreateRoutingProfile, RoutingProfileResponse
from controller.crud import create_user, get_user_by_id, update_user, delete_user, get_all_users
from controller.role_crud import create_role, get_role, get_all_roles, update_role, delete_role
from controller.routing_profile_crud import create_routing_profile, get_all_routing_profiles, get_routing_profile, update_routing_profile, delete_routing_profile
from models.User import Role
from models.User import User
from models.User import RoutingProfile
from routes.team_routes import router as team_router
from routes.user_role_routes import router as user_role_routes
from routes.skill_routes import router as skill_routes
from routes.channel_routes import router as channel_routes
from routes.queue_routes import router as queue_routes
from routes.agent_team_routes import router as agent_team_routes
from routes.routing_profile_channel_routes import router as routing_profile_channel_routes
from datetime import datetime

app = FastAPI()

# Include the team_router from team_routes.py
app.include_router(team_router)
app.include_router(user_role_routes)
app.include_router(skill_routes)
app.include_router(channel_routes)
app.include_router(queue_routes)
app.include_router(agent_team_routes)
app.include_router(routing_profile_channel_routes)
# User API routes

@app.post("/users/")
def create_user_handler(user_data: UserCreate):
    user_data_dict = user_data.dict()
    user = create_user(**user_data_dict)
    return {"message": "User created successfully", "user": user}

@app.get("/users/{user_id}")
def get_user_by_id_handler(user_id: int):
    user = get_user_by_id(user_id)
    if user:
        return {"message": "User found", "user": user}
    else:
        return {"message": "User not found"}

@app.put("/users/{user_id}")
def update_user_handler(user_id: int, user_data: UserCreate):
    user_data_dict = user_data.dict()
    updated_user = update_user(user_id, user_data_dict)
    if updated_user:
        return {"message": "User updated successfully", "user": updated_user}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user_handler(user_id: int):
    deleted_user = delete_user(user_id)
    if deleted_user:
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}

@app.get("/users/", response_model=List[UserResponse])
def get_all_users_handler():
    users = get_all_users()
    user_responses = []
    for user in users:
        updated_at = user.updated_at or datetime.now()
        user_response = UserResponse(
            user_id=user.user_id,
            userid=user.userid,
            password=user.password,
            name=user.name,
            email=user.email,
            role_id=user.role_id,
            extension=user.extension,
            team_id=user.team_id,
            is_active=user.is_active,
            routing_profile_id=user.routing_profile_id,
            created_at=user.created_at,
            updated_at=updated_at
        )
        user_responses.append(user_response)
    return user_responses

# Role API routes

@app.post("/roles/", response_model=CreateRole)
def create_role_handler(role: CreateRole):
    role_data = role.dict()
    created_role = create_role(role_data)
    return created_role

@app.get("/roles/{role_id}", response_model=RoleResponse)
def get_role_handler(role_id: int):
    role = get_role(role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

@app.get("/roles/", response_model=List[RoleResponse])
def get_all_roles_handler():
    return get_all_roles()

@app.put("/roles/{role_id}", response_model=RoleResponse)
def update_role_handler(role_id: int, role: CreateRole):
    role_data = role.dict()
    updated_role = update_role(role_id, role_data)
    if not updated_role:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role

@app.delete("/roles/{role_id}")
def delete_role_handler(role_id: int):
    if not delete_role(role_id):
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}

# RoutingProfile API routes

@app.post("/routing_profiles/", response_model=CreateRoutingProfile)
def create_routing_profile_handler(routing_profile_data: dict):
    return create_routing_profile(routing_profile_data)

@app.get("/routing_profiles/", response_model=List[RoutingProfileResponse])
def get_all_routing_profiles_handler():
    return get_all_routing_profiles()

@app.get("/routing_profiles/{routing_profile_id}", response_model=RoutingProfileResponse)
def get_routing_profile_handler(routing_profile_id: int):
    return get_routing_profile(routing_profile_id)

@app.put("/routing_profiles/{routing_profile_id}", response_model=RoutingProfileResponse)
def update_routing_profile_handler(routing_profile_id: int, routing_profile_data: dict):
    return update_routing_profile(routing_profile_id, routing_profile_data)

@app.delete("/routing_profiles/{routing_profile_id}")
def delete_routing_profile_handler(routing_profile_id: int):
    if not delete_routing_profile(routing_profile_id):
        raise HTTPException(status_code=404, detail="Routing Profile not found")
    return {"message": "Routing Profile deleted successfully"}




