# Referencia: https://fastapi.tiangolo.com/tutorial/sql-databases/#crud-utils
from sqlalchemy.orm import Session

from domain import commentSchema
from model import commentModel

def get_comments_by_video_id(db: Session, video_id: int):
   return db.query(commentModel.Comment).filter(commentModel.Comment.video_id == video_id).all()

def get_comment_by_id(db: Session, id: int):
   return db.query(commentModel.Comment).filter(commentModel.Comment.id == id).first()

def create_comment(db: Session, video_id, user_id, user_name,content):
  db_comment = commentModel.Comment(video_id=video_id, user_id=user_id,user_name=user_name, content=content)
  db.add(db_comment)
  db.commit()
  db.refresh(db_comment)
  return db_comment

def update_comment(db: Session, db_comment: commentSchema.Comment, content: commentSchema.CommentUpdate):
  comment_data = content.dict(exclude_unset=True)
  for key, value in comment_data.items():
    setattr(db_comment, key, value)

  db.add(db_comment)
  db.commit()
  db.refresh(db_comment)
  return db_comment

def delete_comment(db: Session, db_comment: commentSchema.Comment):
  db.delete(db_comment)
  db.commit()