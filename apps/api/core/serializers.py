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

    def validate_fill_level(self, value: float) -> float:
        if value < 0 or value > 100:
            raise serializers.ValidationError("Fill level must be between 0 and 100.")
        return value


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"

    def validate_defect_score(self, value: float) -> float:
        if value < 0 or value > 1:
            raise serializers.ValidationError("Defect score must be between 0 and 1.")
        return value


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = "__all__"