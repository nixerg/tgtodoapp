from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, func

from models import init_db, Task
import requests as rq

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print('Bot is ready')
    yield

app = FastAPI(title="Todo app", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test-cors")
async def test_cors():
    return {"message": "CORS is working"}

@app.get("/api/tasks/{tg_id}")
async def tasks(tg_id: int):
    user = await rq.add_user(tg_id)
    return await rq.get_tasks(user.id)

@app.get('/api/main/{tg_id}')
async def profile(tg_id: int):
    user = await rq.add_user(tg_id)
    count = get_completed_task_count(user.id)
    return {'completedTasks': count}

async def get_completed_task_count(user_id: int):
    async with rq.async_session() as session:
        return await session.scalar(select(func.count(Task.id)).where(Task.completed == True, Task.user_id == user_id))

