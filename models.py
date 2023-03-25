from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import String, Integer, Column, Text, ForeignKey, JSON


class Par(Base):
    __tablename__='param'
    id = Column(Integer, primary_key = True)
    param_1 = Column(Integer)
    param_2 = Column(String)

class Task(Base):
    __tablename__ = 'tasks'
    task_uuid = Column(Integer, primary_key=True)
    description = Column(Text)
    params = Column(Integer)

    def __repr__(self):

       return f"<Task UUID {self.task_uuid} description = {self.description} params = {self.params}"



