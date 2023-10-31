from fastapi import APIRouter, HTTPException, Response, status, Depends
from database import get_db
from sqlalchemy.orm import Session

from domain import commentSchema
from repository import commentRepository

comment = APIRouter(
  prefix="/comments"
)

@comment.get("/{video_id}", response_model=commentSchema.Comment)
def read_comment(video_id: int, db: Session = Depends(get_db)):
  comment = commentRepository.get_comment_by_id(db, video_id)
  if not comment:
    raise HTTPException(status_code=404, detail="erro")
  return comment

