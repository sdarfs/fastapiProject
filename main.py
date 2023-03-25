
from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app = FastAPI()
class Par(BaseModel):
    param_1:int
    param_2: str
class Task(BaseModel):
    task_uuid: int
    description: str
    params: int

    class Config:
        orm_mode=True


db=SessionLocal()

@app.get('/tasks',response_model=List[Task],status_code=200)
def get_all_items():
    items=db.query(models.Task).all()
    return items


@app.post('/tasks/add',response_model=Task,
        status_code=status.HTTP_201_CREATED)
def create_an_item(task:Task):
    db_item=db.query(models.Task).filter(models.Task.task_uuid==task.task_uuid).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Task already exists")

    new_task=models.Task(
        task_uuid=task.task_uuid,
        description=task.description,
        params = task.params

    )

    db.add(new_task)
    db.commit()

@app.put('/tasks/{task_uuid}',response_model=Task,status_code=status.HTTP_200_OK)
def update_an_item(task_uuid:int,task:Task):
    item_to_update=db.query(models.Task).filter(models.Task.task_uuid==task_uuid).first()
    item_to_update.task_uuid=task.task_uuid
    item_to_update.description=task.description
    item_to_update.params = task.params
    db.commit()

    return item_to_update