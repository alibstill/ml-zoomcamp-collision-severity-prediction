from pydantic import BaseModel


class AccidentSeverityResponse(BaseModel):
    severity_probability: float
    is_severe: str
