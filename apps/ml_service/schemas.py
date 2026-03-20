from pydantic import BaseModel, Field, field_validator


class PredictRequest(BaseModel):
    features: list[float] = Field(
        ...,
        min_length=4,
        max_length=4,
        description="A list of 4 numeric features for the tiny classifier.",
        examples=[[0.1, 0.2, 0.1, 0.0]],
    )

    @field_validator("features")
    @classmethod
    def validate_feature_values(cls, values: list[float]) -> list[float]:
        for value in values:
            if not isinstance(value, (int, float)):
                raise ValueError("All feature values must be numeric.")
        return values


class PredictResponse(BaseModel):
    predicted_class: int = Field(..., description="Predicted class index.", examples=[0])
    predicted_label: str = Field(..., description="Predicted class label.", examples=["ok"])
    probabilities: list[float] = Field(
        ...,
        description="Class probabilities in model output order.",
        examples=[[0.72, 0.28]],
    )


class HealthResponse(BaseModel):
    status: str = Field(..., description="Service health state.", examples=["ok"])


class MetadataResponse(BaseModel):
    model_name: str = Field(..., description="Model name.", examples=["tiny_classifier"])
    model_type: str = Field(..., description="Model implementation type.", examples=["pytorch_mlp"])
    class_names: list[str] = Field(..., description="Ordered class labels.", examples=[["ok", "defect"]])
    input_dim: int = Field(..., description="Expected input feature length.", examples=[4])