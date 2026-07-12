from fastapi import FastAPI
import uvicorn
from routers import patients 
app=FastAPI()

app.include_router(patients.router, prefix="/patients",tags=["patients"])

