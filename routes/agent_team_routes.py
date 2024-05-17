from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.User import Agent_Team, User, Team
from models.models import AddAgentToTeamRequest, UpdateAgentTeamRequest, GetAllAgentsResponse
from controller import agent_team_crud
from typing import List
from pydantic import BaseModel

router = APIRouter()


@router.post("/agent_team/{agent_id}/{team_id}")
def add_agent_to_team_handler(request_body: AddAgentToTeamRequest, db: Session = Depends(get_db)):
    agent_team = Agent_Team(agent_id=request_body.agent_id, team_id=request_body.team_id)
    db.add(agent_team)
    db.commit()    
    return agent_team

@router.put("/agent_team/{agent_id}/team/{new_team_id}")
def update_agent_team_handler(agent_id: int, new_team_id: int, db: Session = Depends(get_db)):
    if agent_team_crud.update_agent_team(db, agent_id, new_team_id):
        return {"message": "Agent's team updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Failed to update agent's team")

@router.get("/agents", response_model=List[GetAllAgentsResponse])
def get_all_agents_handler(db: Session = Depends(get_db)):
    agents = agent_team_crud.get_all_agents(db)
    if not agents:
        raise HTTPException(status_code=404, detail="No agents found")
    return agents

@router.delete("/agent/{agent_id}")
def delete_agent_handler(agent_id: int, db: Session = Depends(get_db)):
    if agent_team_crud.delete_agent(db, agent_id):
        return {"message": "Agent deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Agent not found")

