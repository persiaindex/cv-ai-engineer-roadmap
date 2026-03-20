from unittest.mock import patch

from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Inspection, Machine


class PredictionApiTests(APITestCase):
    def setUp(self) -> None:
        self.machine = Machine.objects.create(
            machine_id="M-900",
            name="Prediction Machine",
            location="Aachen Plant",
            is_active=True,
        )
        self.inspection = Inspection.objects.create(
            inspection_id="I-900",
            machine=self.machine,
            defect_score=0.82,
            image_path="data/raw/test.jpg",
            status="defective",
            created_at=timezone.now(),
        )

    @patch("core.views.call_ml_service")
    def test_predict_action_saves_prediction(self, mock_call_ml_service) -> None:
        mock_call_ml_service.return_value = {
            "predicted_class": 1,
            "predicted_label": "defect",
            "probabilities": [0.12, 0.88],
        }

        url = reverse("inspection-predict", args=[self.inspection.id])
        response = self.client.post(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["predicted_label"] == "defect"
        assert response.data["probability_defect"] == 0.88