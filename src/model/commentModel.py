# Referencia: https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base

class Comment(Base):
  __tablename__ = "comments"
  __table_args__ = {'extend_existing': True}

  id = Column(Integer, primary_key=True, index=True)
  video_id = Column(Integer, nullable=False)
  user_id = Column(Integer, nullable=False)
  user_name = Column(String, nullable=False)
  content = Column(String, nullable=False)
  created_at = Column(Date, nullable=False, default=datetime.now()) 
  