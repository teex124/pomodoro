from dataclasses import dataclass
from repository import * 

@dataclass
class TaskService:
    task_cashe: CasheTaskRepository
    task_repository: TaskRepository
    
    def get_tasks(self):
        tasks_cashe = self.task_cashe.get_task()
        if tasks_cashe:
        
            return tasks_cashe
        else:
            tasks = self.task_repository.get_tasks()
            task_schema = [TaskSchema.model_validate(task) for task in tasks]
            self.task_cashe.set_tasks(task_schema)
            return tasks
