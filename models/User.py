from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pydantic import BaseModel
from datetime import datetime



Base = declarative_base()

class User(Base):
    __tablename__ = "Users"

    # user_id = Column(Integer, primary_key=True, autoincrement=True)
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
    user_role = relationship("UserRole", back_populates="user") 

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
    user_role = relationship("UserRole", back_populates="role")
    

class RoutingProfile(Base):
    __tablename__ = "Routing_Profiles"

    routing_profile_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))

    # Define the relationship with User model
    users = relationship("User", back_populates="routing_profile")
    routing_profile_channels = relationship("RoutingProfileChannel", back_populates="routing_profile")


class Team(Base):
    __tablename__ = "Teams"

    team_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    
    users = relationship("User", back_populates="team")


class UserRole(Base):
    __tablename__ = 'user_role'

    user_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('Roles.role_id'), primary_key=True)

    # Define relationships
    user = relationship("User") 
    role = relationship("Role", back_populates="user_role")




class Skills(Base):
    __tablename__ = 'Skills'
    skill_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

class Channels(Base):
    __tablename__ = 'Channels'
    channel_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    routing_profile_channels = relationship("RoutingProfileChannel", back_populates="channel")

class Queues(Base):
    __tablename__ = 'Queues'
    queue_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    wrapup_time = Column(Integer)


# class Agent_Team(Base):
#     __tablename__ = 'Agent_Team'
#     agent_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
#     team_id = Column(Integer, ForeignKey('Teams.team_id'), primary_key=True)

class Agent_Team(Base):
    __tablename__ = 'Agent_Team'

    agent_id = Column(Integer, ForeignKey('Users.user_id'), primary_key=True)
    team_id = Column(Integer, ForeignKey('Teams.team_id'), primary_key=True)

    # Define relationships
    agent = relationship("User")
    team = relationship("Team")

    

class Team_Queue(Base):
    __tablename__ = 'Team_Queue'
    team_id = Column(Integer, ForeignKey('Teams.team_id'), primary_key=True)
    queue_id = Column(Integer, ForeignKey('Queues.queue_id'), primary_key=True)


     # Define relationships
    team = relationship("Team")
    queue = relationship("Queues")

class Customers(Base):
    __tablename__ = 'Customers'
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    address = Column(String(255))
    city = Column(String(50))
    state = Column(String(50))
    zip_code = Column(String(10))
    country = Column(String(50))
    preferred_contact_method = Column(String(20))
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)




class RoutingProfileChannel(Base):
    __tablename__ = "Routing_Profile_Channel"

    routing_profile_id = Column(Integer, ForeignKey("Routing_Profiles.routing_profile_id"), primary_key=True)
    channel_id = Column(Integer, ForeignKey("Channels.channel_id"), primary_key=True)
    max_concurrent_interactions = Column(Integer)
    cross_channel_concurrency = Column(Integer)

    # Define relationships
    channel = relationship("Channels", back_populates="routing_profile_channels")
    routing_profile = relationship("RoutingProfile", back_populates="routing_profile_channels")


class Routing_Profile_Queue_Channel(Base):
    __tablename__ = 'Routing_Profile_Queue_Channel'

    routing_profile_id = Column(Integer, ForeignKey('Routing_Profiles.routing_profile_id'), primary_key=True)
    queue_id = Column(Integer, ForeignKey('Queues.queue_id'), primary_key=True)
    channel_id = Column(Integer, ForeignKey('Channels.channel_id'), primary_key=True)
    queue_priority = Column(Integer)
    queue_delay = Column(Integer)

class Not_Ready_Reason_Codes(Base):
    __tablename__ = 'Not_Ready_Reason_Codes'

    reason_code_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
    is_system_code = Column(Boolean, default=False)

class Wrap_Up_Codes(Base):
    __tablename__ = 'Wrap_Up_Codes'

    wrap_up_code_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))

class Queue_Wrap_Up_Codes(Base):
    __tablename__ = 'Queue_Wrap_Up_Codes'

    queue_id = Column(Integer, ForeignKey('Queues.queue_id'), primary_key=True)
    wrap_up_code_id = Column(Integer, ForeignKey('Wrap_Up_Codes.wrap_up_code_id'), primary_key=True)