import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Table
from datetime import datetime, timezone
import enum

from .database import Base

team_submission = Table

class Submission(Base):
    __tablename__="submissions"
    score = Column()
    timestamp = Column()

class Team(Base):
    __tablename__="teams"
    id = Column()
    hash = Column()
    refemail = Column()
    timestamp = Column()
    

    
    



