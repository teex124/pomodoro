from database import *
from schemas import * 

from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from fastapi import Depends



class TaskRepository:
    
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session
        
    def get_tasks(self):
        with self.db_session() as session: 
            data = session.execute(select(TasksModel)).scalars().all()
        return data
        
    def get_task(self, task_id: int):
        with self.db_session() as session: 
        
            task_model =session.execute(select(TasksModel).where(TasksModel.id == task_id)).scalars().first()
        return task_model
    
    def add_task(self, task: TaskSchema) -> int:
        task_model = TasksModel(name = task.name , pomodoro_count = task.pomodoro_count, category_id = task.category_id)
        with self.db_session() as session: 
            session.add(task_model)
            session.commit()
            return task_model.id
    
    def delete_task(self, task_id: int):
        with self.db_session() as session: 
            session.execute(delete(TasksModel).where(TasksModel.id == task_id)) 
            session.commit()
        return True
    
    def patch_task(self, task_id: int, new_name: str):
        with self.db_session() as session: 
            session.execute(update(TasksModel).where(TasksModel.id == task_id).values(name = new_name))
            session.commit()       
        return True
    
    



