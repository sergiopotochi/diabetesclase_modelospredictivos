from fastapi import FastAPI
from routers import diabetes_router
from schemas.diabetes_schema import PatientData
#from pydantic import BaseModel


app =  FastAPI()
app.include_router(diabetes_router.router)

#class PatientData(BaseModel) : 
#    first_name: str
#    last_name: str
@app.get("/")
async def root():
    return {"message": "Hola Mundo"}

@app.post("/patient")
async def patient(data: PatientData):
    print(data.last_name)
    return{"message": data.first_name}