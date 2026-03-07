from pathlib import Path
import sys
from datetime import datetime


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from domain.feeder import Feeder
from domain.inspection import Inspection
from domain.machine import Machine
from domain.alert import Alert


def test_machine_adds_feeder() -> None:
    machine = Machine(machine_id="M-1", name="Machine 1", location="Aachen")
    machine.add_feeder("F-1")
    assert "F-1" in machine.feeder_ids


def test_feeder_needs_refill() -> None:
    feeder = Feeder(feeder_id="F-1", machine_id="M-1", material_type="powder", fill_level=10.0)
    assert feeder.needs_refill() is True


def test_inspection_detects_defect() -> None:
    inspection = Inspection(
        inspection_id="I-1",
        machine_id="M-1",
        defect_score=0.9,
        image_path="sample.jpg",
        created_at=datetime.now(),
    )
    assert inspection.is_defective() is True


def test_alert_can_close() -> None:
    alert = Alert(
        alert_id="A-1",
        source_type="inspection",
        source_id="I-1",
        message="Problem detected",
        severity="high",
    )
    alert.close()
    assert alert.is_open is False