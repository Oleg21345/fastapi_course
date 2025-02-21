from fastapi import FastAPI
from contextlib import asynccontextmanager
from func_orm import creater_db, drop_db
from route import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_db()
    print("База очищена")
    await creater_db()
    print("База готова")

    yield
    print("Вимкнення")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

















