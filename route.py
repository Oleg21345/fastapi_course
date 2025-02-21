from fastapi.params import Depends
from fastapi import APIRouter
from schemas import STaskAdd, STask, STaskId
from typing import Annotated
from repository import TaskRepository

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],

) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True,
            "task_id": task_id}



@router.get("")
async def get_tasks() -> list[STask]:
    task = await TaskRepository.get_all()
    return {"data": task}


