from sqlalchemy import select, update, delete, func
from models import async_session, User, Task
from pydantic import BaseModel, ConfigDict
from typing import List

class TaskSchema(BaseModel):
    id: int
    title: str
    completed: bool
    user_id: int
    model_config = ConfigDict(from_attributes=True)


async def add_user(tg_id: int):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(tg_id=tg_id)
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user
    
async def get_tasks(user_id: int):
    async with async_session() as session:
        tasks = await session.scalars(select(Task).where(Task.user_id == user_id, Task.completed == False))
        serialized_tasks = [TaskSchema.model_validate(task).model_dump() for task in tasks]
        return serialized_tasks