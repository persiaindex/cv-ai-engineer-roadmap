from typing import Any

import requests
from django.conf import settings



def call_ml_service(features: list[float]) -> dict[str, Any]:
    url = f"{settings.ML_SERVICE_URL}/predict"
    response = requests.post(url, json={"features": features}, timeout=10)
    response.raise_for_status()
    return response.json()