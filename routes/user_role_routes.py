# routes/user_role_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from models.User import UserRole
from models.models import UserRoleRequest

router = APIRouter()


@router.post("/user_role/")
def assign_role_handler(user_role_request: UserRoleRequest, db: Session = Depends(get_db)):
    # Create a new UserRole instance
    user_role = UserRole(user_id=user_role_request.user_id, role_id=user_role_request.role_id)
    # Add the new UserRole to the session and commit the transaction
    db.add(user_role)
    db.commit()
    # Return the created UserRole
    return user_role


@router.delete("/user_role/")
def remove_role_handler(user_role_request: UserRoleRequest, db: Session = Depends(get_db)):
    # Query the UserRole by user_id and role_id
    user_role = db.query(UserRole).filter_by(user_id=user_role_request.user_id, role_id=user_role_request.role_id).first()
    # If the UserRole exists, delete it from the session and commit the transaction
    if user_role:
        db.delete(user_role)
        db.commit()
        return {"message": "User role removed successfully"}
    # If the UserRole does not exist, raise an HTTPException with status code 404
    raise HTTPException(status_code=404, detail="User role not found")

@router.get("/user_role/")
def get_all_user_roles(db: Session = Depends(get_db)):
    return db.query(UserRole).all()


# @router.delete("/user_role/{user_id}/{role_id}")
# def remove_role_handler(user_id: int, role_id: int, db: Session = Depends(get_db)):
#     # Query the UserRole by user_id and role_id
#     user_role = db.query(UserRole).filter_by(user_id=user_id, role_id=role_id).first()
#     # If the UserRole exists, delete it from the session and commit the transaction
#     if user_role:
#         db.delete(user_role)
#         db.commit()
#         return {"message": "User role removed successfully"}
#     # If the UserRole does not exist, raise an HTTPException with status code 404
#     raise HTTPException(status_code=404, detail="User role not found")
