from sqlalchemy.orm import Session
from config.database import SessionLocal
from models.User import RoutingProfile
from fastapi import HTTPException

def create_routing_profile(routing_profile_data: dict):
    db = SessionLocal()
    new_routing_profile = RoutingProfile(**routing_profile_data)
    db.add(new_routing_profile)
    db.commit()
    db.refresh(new_routing_profile)
    return new_routing_profile

def get_all_routing_profiles():
    db = SessionLocal()
    return db.query(RoutingProfile).all()

def get_routing_profile(routing_profile_id: int):
    db = SessionLocal()
    routing_profile = db.query(RoutingProfile).filter(RoutingProfile.routing_profile_id == routing_profile_id).first()
    if not routing_profile:
        raise HTTPException(status_code=404, detail="Routing Profile not found")
    return routing_profile

def update_routing_profile(routing_profile_id: int, routing_profile_data: dict):
    db = SessionLocal()
    routing_profile = db.query(RoutingProfile).filter(RoutingProfile.routing_profile_id == routing_profile_id).first()
    if routing_profile:
        for key, value in routing_profile_data.items():
            setattr(routing_profile, key, value)
        db.commit()
        db.refresh(routing_profile)
    return routing_profile

def delete_routing_profile(routing_profile_id: int):
    db = SessionLocal()
    routing_profile = db.query(RoutingProfile).filter(RoutingProfile.routing_profile_id == routing_profile_id).first()
    if routing_profile:
        db.delete(routing_profile)
        db.commit()
        return True
    return False
