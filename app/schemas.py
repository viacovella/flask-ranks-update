from pydantic import BaseModel, Typing, EmailStr
from datetime import datetime

# Schemas for Teams

class TeamBase(BaseModel):
	shortname:str = Field(min_length = 8, max_length=8)
	extendedname:Optional[str]
	refemail:EmailStr

	
	@field_validator('shortname')
	def validate_username(cls, v:str) -> str:
		if not len(v)==8:
			raise ValueError('shortname must be 8 characters long')
		if not v.isalnum():
			raise ValueError('shortname must be alphanumeric')
			
		return v.lower()
		
class TeamCreate(TeamBase):
	pass
	
class TeamUpdate(TeamBase):
	shortname:str = Field(None)
	extendedname:Optional[str]
	refemail:Optional[EmailStr]
	
class TeamRead(TeamBase):
	id: int 
	created_at: datetime
	
# Schemas for Submissions

class SubmissionBase(BaseModel):
	score:float=Field(gt=0,lt=100)
	
class SubmissionCreate(SubmissionBase):
	pass

class SubmissionUpdate(SubmissionBase):
	score:Optional[float]
	
class SubmissionRead(SubmissionBase):
	id:int 
	created_at:datetime
