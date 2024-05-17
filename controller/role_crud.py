from sqlalchemy.orm import Session
from config.database import SessionLocal
from models.User import Role
from fastapi import HTTPException

def create_role(role_data: dict):
    db = SessionLocal()
    new_role = Role(**role_data)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_all_roles():
    db = SessionLocal()
    return db.query(Role).all()

def get_role(role_id: int):
    db = SessionLocal()
    role = db.query(Role).filter(Role.role_id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    return role

def update_role(role_id: int, role_data: dict):
    db = SessionLocal()
    role = db.query(Role).filter(Role.role_id == role_id).first()
    if role:
        for key, value in role_data.items():
            setattr(role, key, value)
        db.commit()
        db.refresh(role)
    return role

def delete_role(role_id: int):
    db = SessionLocal()
    role = db.query(Role).filter(Role.role_id == role_id).first()
    if role:
        db.delete(role)
        db.commit()
        return True
    return False
