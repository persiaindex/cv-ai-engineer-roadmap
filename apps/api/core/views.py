
from rest_framework import status

from .ml_client import call_ml_service
from .models import MLPrediction
from .serializers import MLPredictionSerializer

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Alert, Feeder, Inspection, Machine
from .serializers import (
    AlertSerializer,
    FeederSerializer,
    InspectionSerializer,
    MachineSerializer,
)
from .services import get_dashboard_summary

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all().order_by("machine_id")
    serializer_class = MachineSerializer
    filterset_fields = ["location", "is_active"]
    search_fields = ["machine_id", "name", "location"]
    ordering_fields = ["machine_id", "created_at", "name"]


class FeederViewSet(viewsets.ModelViewSet):
    queryset = Feeder.objects.all().order_by("feeder_id")
    serializer_class = FeederSerializer
    filterset_fields = ["material_type", "machine"]
    search_fields = ["feeder_id", "material_type", "machine__machine_id"]
    ordering_fields = ["feeder_id", "fill_level", "created_at"]


class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all().order_by("-created_at")
    serializer_class = InspectionSerializer
    filterset_fields = ["status", "machine"]
    search_fields = ["inspection_id", "status", "machine__machine_id"]
    ordering_fields = ["created_at", "defect_score", "inspection_id"]
    @action(detail=True, methods=["post"], url_path="predict")
    def predict(self, request, pk=None):
        inspection = self.get_object()

        features = [
            float(inspection.defect_score),
            1.0 if inspection.status == "defective" else 0.0,
            1.0 if inspection.status == "review" else 0.0,
            1.0 if inspection.status == "ok" else 0.0,
        ]

        ml_result = call_ml_service(features)

        prediction, _ = MLPrediction.objects.update_or_create(
            inspection=inspection,
            defaults={
                "predicted_class": ml_result["predicted_class"],
                "predicted_label": ml_result["predicted_label"],
                "probability_ok": ml_result["probabilities"][0],
                "probability_defect": ml_result["probabilities"][1],
            },
        )

        serializer = MLPredictionSerializer(prediction)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by("-created_at")
    serializer_class = AlertSerializer
    filterset_fields = ["severity", "is_open", "source_type"]
    search_fields = ["alert_id", "source_type", "source_id", "severity"]
    ordering_fields = ["created_at", "severity", "alert_id"]
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def close(self, request, pk=None):
        alert = self.get_object()
        alert.is_open = False
        alert.save()
        return Response({
            "message": f"Alert {alert.alert_id} closed successfully.",
            "is_open": alert.is_open,
        })

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def dashboard_summary(request):
    return Response(get_dashboard_summary())