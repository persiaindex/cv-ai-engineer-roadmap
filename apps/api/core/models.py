from django.db import models


class Machine(models.Model):
    machine_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.machine_id} - {self.name}"


class Feeder(models.Model):
    feeder_id = models.CharField(max_length=20, unique=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="feeders")
    material_type = models.CharField(max_length=50)
    fill_level = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.feeder_id} ({self.machine.machine_id})"


class Inspection(models.Model):
    STATUS_CHOICES = [
        ("ok", "OK"),
        ("review", "Review"),
        ("defective", "Defective"),
    ]

    inspection_id = models.CharField(max_length=20, unique=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name="inspections")
    defect_score = models.FloatField()
    image_path = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.inspection_id} - {self.status}"


class Alert(models.Model):
    SEVERITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    alert_id = models.CharField(max_length=20, unique=True)
    source_type = models.CharField(max_length=20)
    source_id = models.CharField(max_length=20)
    message = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.alert_id} - {self.severity}"