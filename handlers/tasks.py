from database import *
from schemas import *
from repository import *
from depends import *
from service import *

from fastapi import APIRouter, Depends
from typing import Annotated



router = APIRouter(prefix='/task', tags=['task'])
 

@router.get(
    '/all', response_model=list[TaskSchema])
async def get_tasks(
        tasks_servece: Annotated[TaskService, Depends(get_task_service)]
    ):
    return tasks_servece.get_tasks()

@router.post('/', 
              response_model=TaskSchema)
async def create_task(
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
        task: TaskSchema
    ):
    task_id = task_repository.add_task(task)
    task = task_repository.get_task(task_id=task_id)
    return task
    
@router.patch('/patch',
              response_model=TaskSchema)
async def patch_task(
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
        id: int,
        new_name: str
    ):
    task_repository.patch_task(task_id=id, new_name=new_name)
    task = task_repository.get_task(task_id=id)
    return task

@router.delete('/delete')
async def delete_task(
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)],
        id: int
    ):
    task_repository.delete_task(task_id=id)
    
    