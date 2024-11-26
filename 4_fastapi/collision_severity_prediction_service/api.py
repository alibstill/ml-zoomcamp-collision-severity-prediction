from fastapi import FastAPI, Depends
from functools import lru_cache
from .app_settings import AppSettings
from typing_extensions import Annotated
from .prediction_service import PredictionService
from .accident_severity_response import AccidentSeverityResponse
from .collision_request import CollisionRequest

app = FastAPI(title="Collision Severity Prediction Service")


@lru_cache
def get_app_settings():
    return AppSettings()


def get_prediction_service(settings: Annotated[AppSettings, Depends(get_app_settings)]):
    return PredictionService(model_file_name=settings.ml_model_filename)


@app.post(
    "/accident_severity",
    response_model=AccidentSeverityResponse,
    status_code=200,
    tags=["core"],
)
async def get_accident_severity(
    request: CollisionRequest,
    prediction_service: Annotated[PredictionService, Depends(get_prediction_service)],
):
    pred, is_severe = prediction_service.predict_severity(collision=request.dict())
    return AccidentSeverityResponse(severity_probability=pred, is_severe=is_severe)
