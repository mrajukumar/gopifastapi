from sqlalchemy.orm import sessionmaker
from models.User import User
from sqlalchemy import create_engine
import mysql.connector


# Define the connection details
DB_NAME = "test"
DB_USER = "root"
DB_PASSWORD = "123456789"
DB_HOST = "localhost"
DB_PORT = "3306"


mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD,
  database=DB_NAME
)


# Define the database URL
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_all_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users


def create_user(userid, password, name, email, role_id, extension=None, team_id=None, is_active=True, routing_profile_id=None):
    db = SessionLocal()
    db_user = User(userid=userid, password=password, name=name, email=email, role_id=role_id,
                   extension=extension, team_id=team_id, is_active=is_active, routing_profile_id=routing_profile_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

def get_user_by_id(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == user_id).first()
    db.close()
    return user

def update_user(user_id, data):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == user_id).first()
    for key, value in data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    db.close()
    return {"message": "User deleted successfully"}
