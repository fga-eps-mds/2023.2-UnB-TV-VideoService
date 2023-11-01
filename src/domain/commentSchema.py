from datetime import date
from pydantic import BaseModel, ConfigDict

class CommentUpdate(BaseModel):
  content: str | None = None

class Comment(BaseModel):
  model_config = ConfigDict(from_attributes = True)
  id: int
  user_id: int
  video_id: int
  content: str
  created_at: date

class CommentCreate(BaseModel):
  model_config = ConfigDict(from_attributes = True)
  user_id: int
  video_id: int
  content: str
  