from datetime import datetime

from domain.alert import Alert
from domain.feeder import Feeder
from domain.inspection import Inspection
from domain.machine import Machine


def build_demo_scenario() -> None:
    machine = Machine(
        machine_id="M-100",
        name="Smart Feeder Line A",
        location="Aachen Plant 1",
    )

    feeder = Feeder(
        feeder_id="F-200",
        machine_id=machine.machine_id,
        material_type="powder",
        fill_level=15.0,
    )

    inspection = Inspection(
        inspection_id="I-300",
        machine_id=machine.machine_id,
        defect_score=0.82,
        image_path="data/raw/sample_inspection.jpg",
        created_at=datetime.now(),
    )

    machine.add_feeder(feeder.feeder_id)

    alerts = []

    if feeder.needs_refill():
        alerts.append(
            Alert(
                alert_id="A-400",
                source_type="feeder",
                source_id=feeder.feeder_id,
                message="Feeder fill level is below threshold.",
                severity="medium",
            )
        )

    if inspection.is_defective():
        alerts.append(
            Alert(
                alert_id="A-401",
                source_type="inspection",
                source_id=inspection.inspection_id,
                message="Defect score exceeded threshold.",
                severity="high",
            )
        )

    print("Machine:", machine)
    print("Feeder:", feeder)
    print("Inspection:", inspection)
    print("Alerts:")
    for alert in alerts:
        print(alert)


if __name__ == "__main__":
    build_demo_scenario()
    