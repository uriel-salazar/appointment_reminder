from fastapi import FastAPI
import uvicorn
from database.db import Base, engine
from routers import appointments, patients

app = FastAPI()
Base.metadata.create_all(bind = engine)

app.include_router(patients.router, prefix="/patients",tags=["patients"])
app.include_router(appointments.router,prefix="/appointments",tags=["appointments"])



if __name__ == "__main__":
    uvicorn.run("main:app", 
            host="localhost", reload=True)