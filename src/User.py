from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    role_id = Column(Integer, ForeignKey("Roles.role_id"), nullable=False)
    extension = Column(String(10))
    team_id = Column(Integer, ForeignKey("Teams.team_id"))
    is_active = Column(Boolean, default=True)
    routing_profile_id = Column(Integer, ForeignKey("Routing_Profiles.routing_profile_id"))
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    # Relationships
    role = relationship("Role", back_populates="users")
    team = relationship("Team", back_populates="users")
    routing_profile = relationship("RoutingProfile", back_populates="users")

    def __get_pydantic_core_schema__(cls, model_name: str):
        # Implement logic to generate the Pydantic schema for your class
        schema = {}
        for column in cls.__table__.columns:
            schema[column.name] = getattr(BaseModel, column.type.python_type.__name__)
        return schema

        
class Role(Base):
    __tablename__ = "Roles"

    role_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

     # Define the relationship with User model
    users = relationship("User", back_populates="role")

class RoutingProfile(Base):
    __tablename__ = "Routing_Profiles"

    routing_profile_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))

    # Define the relationship with User model
    users = relationship("User", back_populates="routing_profile")


class Team(Base):
    __tablename__ = "Teams"

    team_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    
    users = relationship("User", back_populates="team")


#=================================================================
class User_Role(Base):
    __tablename__ = 'User_Role'
    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('Roles.role_id'), primary_key=True)

class Skills(Base):
    __tablename__ = 'Skills'
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

class Channels(Base):
    __tablename__ = 'Channels'
    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

class Queues(Base):
    __tablename__ = 'Queues'
    queue_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    wrapup_time = Column(Integer)