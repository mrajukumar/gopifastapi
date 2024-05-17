from sqlalchemy.orm import Session
from models.User import User
from models.User import Role
from models.User import UserRole

def assign_role(db: Session, user_id: int, role_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    role = db.query(Role).filter(Role.id == role_id).first()
    if not user or not role:
        return None  # Or handle the error accordingly
    new_user_role = UserRole(user=user, role=role)
    db.add(new_user_role)
    db.commit()
    db.refresh(new_user_role)
    return new_user_role


def remove_role(user_id: int, role_id: int):
    user_role = User_Role.query.filter_by(user_id=user_id, role_id=role_id).first()
    if user_role:
        user_role.delete()
        return True
    return False


def get_all_user_roles(db: Session = Depends(get_db)):
    return db.query(UserRole).all()
