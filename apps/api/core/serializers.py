from rest_framework import serializers

from .models import Alert, Feeder, Inspection, Machine


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"


class FeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeder
        fields = "__all__"


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = "__all__"