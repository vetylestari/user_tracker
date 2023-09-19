# model/database.py
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'DATABASE_URL' with your actual database URL
# Gantilah nilai-nilai berikut sesuai dengan konfigurasi PostgreSQL Anda
username = 'postgres'
password = 'renos123!!'
hostname = 'localhost'  # Ganti dengan alamat server PostgreSQL Anda jika berbeda
port = '5433'  # Port default PostgreSQL
database_name = 'postgres'

DATABASE_URL = f'postgres://{username}:{password}@{hostname}:{port}/{database_name}'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserResponse(Base):
    __tablename__ = "user_responses"

    id = Column(Integer, primary_key=True, index=True)
    host = Column(String, nullable=False)
    user_agent = Column(String, nullable=False)
    client_host = Column(String, nullable=False)
    client_port = Column(Integer, nullable=False)
    client_browser = Column(String, nullable=False)
    client_os = Column(String, nullable=False)
    client_device = Column(String, nullable=False)
    is_bot = Column(Boolean, nullable=False)
    is_email_client = Column(Boolean, nullable=False)
    is_mobile = Column(Boolean, nullable=False)
    is_pc = Column(Boolean, nullable=False)
    is_tablet = Column(Boolean, nullable=False)
    is_touch_capable = Column(Boolean, nullable=False)
    custom_user = Column(String, nullable=False, default='')