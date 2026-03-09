from django.test import TestCase
from django.utils import timezone

from .models import Alert, Feeder, Inspection, Machine


class MachineModelTest(TestCase):
    def test_create_machine(self) -> None:
        machine = Machine.objects.create(
            machine_id="M-200",
            name="Test Machine",
            location="Aachen",
            is_active=True,
        )
        self.assertEqual(machine.machine_id, "M-200")
        self.assertTrue(machine.is_active)


class FeederModelTest(TestCase):
    def test_create_feeder_for_machine(self) -> None:
        machine = Machine.objects.create(
            machine_id="M-201",
            name="Machine With Feeder",
            location="Aachen",
        )
        feeder = Feeder.objects.create(
            feeder_id="F-201",
            machine=machine,
            material_type="powder",
            fill_level=25.0,
        )
        self.assertEqual(feeder.machine, machine)
        self.assertEqual(feeder.material_type, "powder")


class InspectionModelTest(TestCase):
    def test_create_inspection(self) -> None:
        machine = Machine.objects.create(
            machine_id="M-202",
            name="Inspection Machine",
            location="Aachen",
        )
        inspection = Inspection.objects.create(
            inspection_id="I-202",
            machine=machine,
            defect_score=0.81,
            image_path="data/raw/test.jpg",
            status="defective",
            created_at=timezone.now(),
        )
        self.assertEqual(inspection.status, "defective")
        self.assertGreaterEqual(inspection.defect_score, 0.8)


class AlertModelTest(TestCase):
    def test_create_alert(self) -> None:
        alert = Alert.objects.create(
            alert_id="A-202",
            source_type="inspection",
            source_id="I-202",
            message="Defect score exceeded threshold.",
            severity="high",
            is_open=True,
        )
        self.assertEqual(alert.severity, "high")
        self.assertTrue(alert.is_open)