from sqlalchemy.orm import Session
from models.User import Skills


def create_skill(db: Session, name: str):
    """
    Create a new skill.
    """
    skill = Skills(name=name)
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill


def get_skill(db: Session, skill_id: int):
    """
    Retrieve a skill by its ID.
    """
    return db.query(Skills).filter(Skills.skill_id == skill_id).first()


def get_skill_by_name(db: Session, name: str):
    """
    Retrieve a skill by its name.
    """
    return db.query(Skills).filter(Skills.name == name).first()


def get_all_skills(db: Session):
    """
    Retrieve all skills.
    """
    return db.query(Skills).all()


def update_skill(db: Session, skill_id: int, name: str):
    """
    Update a skill's name by its ID.
    """
    skill = db.query(Skills).filter(Skills.skill_id == skill_id).first()
    if skill:
        skill.name = name
        db.commit()
        db.refresh(skill)
        return skill
    return None


def delete_skill(db: Session, skill_id: int):
    """
    Delete a skill by its ID.
    """
    skill = db.query(Skills).filter(Skills.skill_id == skill_id).first()
    if skill:
        db.delete(skill)
        db.commit()
        return True
    return False
