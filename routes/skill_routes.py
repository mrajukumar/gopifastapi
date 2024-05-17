from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import SkillCreate, SkillUpdate, SkillOut
from controller import skill_crud
from typing import List

router = APIRouter()

@router.post("/skills/", response_model=SkillOut)
def create_skill(skill_data: SkillCreate, db: Session = Depends(get_db)):
    """
    Create a new skill.
    """
    skill = skill_crud.create_skill(db, name=skill_data.name)
    return skill

@router.get("/skills/{skill_id}", response_model=SkillOut)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a skill by its ID.
    """
    skill = skill_crud.get_skill(db, skill_id)
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.get("/skills/", response_model=List[SkillOut])
def read_all_skills(db: Session = Depends(get_db)):
    """
    Retrieve all skills.
    """
    skills = skill_crud.get_all_skills(db)
    return skills

@router.put("/skills/{skill_id}", response_model=SkillOut)
def update_skill(skill_id: int, skill_data: SkillUpdate, db: Session = Depends(get_db)):
    """
    Update a skill by its ID.
    """
    skill = skill_crud.update_skill(db, skill_id, name=skill_data.name)
    if skill is None:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@router.delete("/skills/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    """
    Delete a skill by its ID.
    """
    deleted = skill_crud.delete_skill(db, skill_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"message": "Skill deleted successfully"}
