import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the connection details
DB_NAME = "ZConnectDB"
DB_USER = "ZConnect"
DB_PASSWORD = "Zeniusit123"
DB_HOST = "localhost"
DB_PORT = "3306"

# Connect to the MySQL database using mysql.connector
mydb = mysql.connector.connect(
  host=DB_HOST,
  user=DB_USER,
  password=DB_PASSWORD,
  database=DB_NAME
)

# Define the database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the database engine using SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a sessionmaker object for SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
