from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.db.session import create_db_and_tables

# Import models and ensure the are registered with SQLModel metadata
from app.models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables
    create_db_and_tables()
    yield
    # Shutdown: Clean resources if needed (not needed for now)

app = FastAPI(
  title=settings.PROJECT_NAME,
  lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}