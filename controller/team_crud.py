from sqlalchemy.orm import Session
from fastapi import HTTPException
from config.database import SessionLocal
from models.User import Team

def create_team(team_data: dict):
    db = SessionLocal()
    new_team = Team(**team_data)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

def get_all_teams():
    db = SessionLocal()
    return db.query(Team).all()

def get_team(team_id: int):
    db = SessionLocal()
    team = db.query(Team).filter(Team.team_id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

def update_team(team_id: int, team_data: dict):
    db = SessionLocal()
    team = db.query(Team).filter(Team.team_id == team_id).first()
    if team:
        for key, value in team_data.items():
            setattr(team, key, value)
        db.commit()
        db.refresh(team)
    return team

def delete_team(team_id: int):
    db = SessionLocal()
    team = db.query(Team).filter(Team.team_id == team_id).first()
    if team:
        db.delete(team)
        db.commit()
        return True
    return False
