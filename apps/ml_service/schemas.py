from pydantic import BaseModel


class PredictRequest(BaseModel):
    features: list[float]


class PredictResponse(BaseModel):
    predicted_class: int
    predicted_label: str
    probabilities: list[float]


class HealthResponse(BaseModel):
    status: str


class MetadataResponse(BaseModel):
    model_name: str
    model_type: str
    class_names: list[str]
    input_dim: int