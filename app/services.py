from sqlalchemy.orm import Session
from . import models, schemas

# creare una submission
def create_submission(db: Session, submission: schemas.SubmissionCreate, team_id: int):
    # object crearion
    db_submission = models.Submission(
        score=submission.score,
        team_id=team_id,
        
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

# single team history
def get_team_history(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def get_leaderboard(db: Session):
    return db.query(models.Team).all()
