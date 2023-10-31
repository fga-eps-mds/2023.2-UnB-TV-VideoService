from fastapi import APIRouter, HTTPException, Response, status, Depends
from database import get_db
from sqlalchemy.orm import Session

from domain import commentSchema
from repository import commentRepository

comment = APIRouter(
  prefix="/comments"
)


@comment.get("/{video_id}", response_model=list[commentSchema.Comment])
def read_comment(video_id: int, db: Session = Depends(get_db)):
  comment = commentRepository.get_comment_by_id(db, video_id=video_id)
  if not comment:
    raise HTTPException(status_code=404, detail="erro")
  return comment

@comment.post("/", response_model=commentSchema.Comment)
def create_comment(comment: commentSchema.CommentCreate, db: Session = Depends(get_db)):
  print(comment)
  return commentRepository.create_comment(db=db, video_id=comment.video_id, user_id=comment.user_id, content=comment.content)
