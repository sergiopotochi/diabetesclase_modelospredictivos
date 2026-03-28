from fastapi import APIRouter
from schemas.diabetes_schema import PatientData, PatientDiabetesData, PatientDiabetesOutput
from services.diabetes_service import diabetes_prediction
router = APIRouter()

@router.post("/predict")
async def predict(data: PatientDiabetesData): 
    #prediction = "Sano"
    prediction = diabetes_prediction(data)


    resultado = PatientDiabetesOutput(
        first_name=data.first_name,
        last_name=data.last_name,
        prediction=prediction
    )

    return resultado