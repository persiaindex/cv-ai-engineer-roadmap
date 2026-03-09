from django.shortcuts import render

from rest_framework import viewsets

from .models import Alert, Feeder, Inspection, Machine
from .serializers import (
    AlertSerializer,
    FeederSerializer,
    InspectionSerializer,
    MachineSerializer,
)


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all().order_by("machine_id")
    serializer_class = MachineSerializer


class FeederViewSet(viewsets.ModelViewSet):
    queryset = Feeder.objects.all().order_by("feeder_id")
    serializer_class = FeederSerializer


class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all().order_by("-created_at")
    serializer_class = InspectionSerializer


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all().order_by("-created_at")
    serializer_class = AlertSerializer