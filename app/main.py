from fastapi import FastAPI
from .models import Base
from routes import router
from .config import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/data", tags=["data"])


