from fastapi import FastAPI
from app.services.consumer import start_consumer
from threading import Thread

app = FastAPI()
# Including the router
@app.on_event("startup")
def startup_event():
    Thread(target=start_consumer, daemon=True).start()

@app.get("/")
def root():
    return {"status": "ok"}