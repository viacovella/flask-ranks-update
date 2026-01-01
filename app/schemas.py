from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional, List
from datetime import datetime


# Submission Schemas

class SubmissionBase(BaseModel):
    score: float = Field(gt=0, lt=100)

class SubmissionCreate(SubmissionBase):
    pass

class SubmissionRead(SubmissionBase):
    id: int
    sent_at: datetime
    team_id: int 

    class Config:
        from_attributes = True 

# Team Schemas

class TeamBase(BaseModel):
    shortname: str = Field(min_length=8, max_length=8)
    extendedname: Optional[str] = None
    refemail: EmailStr

    @field_validator('shortname')
    def validate_shortname(cls, v: str) -> str:
        if not v.isalnum():
            raise ValueError('shortname must be alphanumeric')
        return v.lower()

class TeamCreate(TeamBase):
    pass

class TeamRead(TeamBase):
    id: int
    
    class Config:
        from_attributes = True

# TeamWithSubmission

class TeamWithSubmissions(TeamRead):
    submissions: List[SubmissionRead] = [] 
