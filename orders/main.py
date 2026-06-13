from fastapi import FastAPI
from app.api.api import router

app = FastAPI()
# Including the router
app.include_router(router, prefix="/api/v1")