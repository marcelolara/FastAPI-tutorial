from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.db.session import create_db_and_tables

# Import models
from app.models.user import User

# Import routes
from app.api import routes

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: create tables
    create_db_and_tables()
    yield
    # Shutdown

app = FastAPI(
  title=settings.PROJECT_NAME,
  lifespan=lifespan
)

# Include the router
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}