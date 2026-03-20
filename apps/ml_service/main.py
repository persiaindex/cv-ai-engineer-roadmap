from fastapi import FastAPI

from .schemas import HealthResponse, MetadataResponse, PredictRequest, PredictResponse
from .service import get_metadata, predict_from_features


app = FastAPI(title="ML Service", version="1.0.0")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/metadata", response_model=MetadataResponse)
def metadata() -> MetadataResponse:
    return MetadataResponse(**get_metadata())


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest) -> PredictResponse:
    result = predict_from_features(request.features)
    return PredictResponse(**result)