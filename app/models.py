import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, DateTime, relationship
from datetime import datetime, timezone
import enum

from .database import Base

class Team(Base):
	__tablename__="teams"
	id = Column(Integer, nullable=False, primary_key=True, index=True)
	shortname = Column(String, nullable =False)
	extendedname = Column(String)
	refemail = Column(String, nullable=False)
	submissions = relationship("Submission", back_populates="team")

class Submission(Base):
	__tablename__="submissions"
	id = Column(Integer, nullable=False, primary_key=True, index=True)
	score = Column(Float)
	sent_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
	team = relationship("Team", back_populates="Submissions").   