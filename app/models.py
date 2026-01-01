from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from .database import Base

class Team(Base):
    __tablename__ = "teams"
    
    id = Column(Integer, primary_key=True, index=True)
    shortname = Column(String, nullable=False)
    extendedname = Column(String)
    refemail = Column(String, nullable=False)
    
    # back population
    submissions = relationship("Submission", back_populates="team") 

class Submission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float)
    sent_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False) 

    team = relationship("Team", back_populates="submissions")
