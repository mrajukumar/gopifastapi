from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.User import Agent_Team, User, Team
from typing import List
import logging


# Create a logger
logger = logging.getLogger(__name__)

def add_agent_to_team(db: Session, agent_id: int, team_id: int):   
    user = db.query(User).filter(User.user_id == agent_id).first()
    team = db.query(Team).filter(Team.team_id == team_id).first()  
    if user and team:       
        agent_team = Agent_Team(user=user, team=team)       
        db.add(agent_team)       
        db.commit()        
        db.refresh(agent_team)
       
        logger.info(f"Agent {user.name} added to team {team.name}")
       
        return agent_team
    elif not user:
        logger.error(f"Failed to add agent to team: User with ID {agent_id} not found")
    elif not team:
        logger.error(f"Failed to add agent to team: Team with ID {team_id} not found")   
    return None


def get_all_agents(db: Session = Depends(get_db)) -> List[Agent_Team]:   
    return db.query(Agent_Team).all()

def update_agent_team(db: Session, agent_id: int, new_team_id: int) -> bool:  
    agent_team = db.query(Agent_Team).filter(Agent_Team.agent_id == agent_id).first()
    if agent_team:
        team = db.query(Team).filter(Team.team_id == new_team_id).first()
        if team:
            agent_team.team_id = new_team_id
            db.commit()
            return True
        else:
            logger.error(f"Failed to update agent's team: Team with ID {new_team_id} not found")
            return False
    else:
        logger.error(f"Failed to update agent's team: Agent with ID {agent_id} not found")
        return False

def delete_agent(db: Session, agent_id: int) -> bool:  
    agent = db.query(User).filter(User.user_id == agent_id).first()
    if agent:
        db.delete(agent)
        db.commit()
        return True
    else:
        logger.error(f"Failed to delete agent: Agent with ID {agent_id} not found")
        return False
