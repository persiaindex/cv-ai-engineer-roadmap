from pathlib import Path
import sys

from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = PROJECT_ROOT / "apps"

if str(APPS_PATH) not in sys.path:
    sys.path.insert(0, str(APPS_PATH))

from ml_service.main import app


client = TestClient(app)



def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"



def test_metadata_endpoint() -> None:
    response = client.get("/metadata")
    assert response.status_code == 200
    payload = response.json()
    assert payload["model_name"] == "tiny_classifier"
    assert payload["input_dim"] == 4



def test_predict_endpoint_returns_prediction() -> None:
    response = client.post("/predict", json={"features": [0.1, 0.2, 0.1, 0.0]})
    assert response.status_code == 200
    payload = response.json()
    assert "predicted_class" in payload
    assert "probabilities" in payload
    assert len(payload["probabilities"]) == 2



def test_predict_endpoint_rejects_wrong_length() -> None:
    response = client.post("/predict", json={"features": [0.1, 0.2]})
    assert response.status_code == 400