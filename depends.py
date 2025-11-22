from database import get_session
from repository import TaskRepository, CasheTaskRepository
from cashe import *
from service import *

from fastapi import Depends
from typing import Annotated

def get_task_repository() -> TaskRepository:
    db_session = get_session()
    return TaskRepository(db_session)


def get_task_cashe_repository() -> CasheTaskRepository:
    redis_connection = get_redis_connection()
    return CasheTaskRepository(redis_connection)
    

def get_task_service(task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
                                                task_cashe: Annotated[CasheTaskRepository, Depends(get_task_cashe_repository)]
                                               ) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        task_cashe=task_cashe
    )     
