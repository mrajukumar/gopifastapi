from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  # Import Session
from typing import List
from User import Team
from models import TeamCreate, TeamUpdate, TeamResponse
from team_crud import create_team, get_all_teams, get_team, update_team, delete_team

router = APIRouter()

@router.post("/teams/", response_model=TeamCreate)
def create_team_handler(team: TeamCreate):
    team_data = team.dict()
    created_team = create_team(team_data)
    return created_team

@router.get("/teams/", response_model=List[TeamResponse])
def get_all_teams_handler():
    return get_all_teams()

@router.get("/teams/{team_id}", response_model=TeamResponse)
def get_team_handler(team_id: int):
    team = get_team(team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.put("/teams/{team_id}", response_model=TeamUpdate)
def update_team_handler(team_id: int, team: TeamUpdate):
    team_data = team.dict()
    updated_team = update_team(team_id, team_data)
    if not updated_team:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated_team

@router.delete("/teams/{team_id}")
def delete_team_handler(team_id: int):   
    if not delete_team(team_id):
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted successfully"}
