from fastapi import APIRouter, HTTPException, Response, status, Depends
from database import get_db
from sqlalchemy.orm import Session

from domain import commentSchema
from repository import commentRepository
from constants import errorMessages

comment = APIRouter(
  prefix="/comments"
)

@comment.get("/{video_id}", response_model=list[commentSchema.Comment])
def read_comment(video_id: int, db: Session = Depends(get_db)):
  comment = commentRepository.get_comments_by_video_id(db, video_id=video_id)
  return comment

@comment.post("/", response_model=commentSchema.Comment)
def create_comment(comment: commentSchema.CommentCreate, db: Session = Depends(get_db)):
  return commentRepository.create_comment(db=db, video_id=comment.video_id, user_id=comment.user_id, user_name= comment.user_name ,content=comment.content)

@comment.delete("/{id}", response_model=commentSchema.Comment)
def delete_comment(id: int, db: Session = Depends(get_db)):
  comment = commentRepository.get_comment_by_id(db, id)
  if not comment:
    raise HTTPException(status_code=404, detail=errorMessages.COMMENT_NOT_FOUND)
  commentRepository.delete_comment(db,comment)
  return comment

@comment.patch("/{id}", response_model=commentSchema.Comment)
def update_comment(id: int, data: commentSchema.CommentUpdate,db: Session = Depends(get_db)):
  comment = commentRepository.get_comment_by_id(db, id)
  if not comment:
    raise HTTPException(status_code=404, detail=errorMessages.COMMENT_NOT_FOUND)
  updated_comment = commentRepository.update_comment(db,comment,data)
  return updated_comment
