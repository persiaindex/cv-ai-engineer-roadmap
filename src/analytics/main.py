from pathlib import Path

from analytics.cleaners import clean_inspection_data, clean_sensor_data
from analytics.loaders import load_csv
from analytics.metrics import (
    build_machine_summary,
    compute_inspection_kpis,
    compute_sensor_kpis,
)


def run_pipeline(project_root: Path) -> None:
    sensor_path = project_root / "data" / "raw" / "sensor_readings.csv"
    inspection_path = project_root / "data" / "raw" / "inspection_results.csv"
    output_path = project_root / "data" / "processed" / "machine_summary.csv"

    sensor_df = clean_sensor_data(load_csv(sensor_path))
    inspection_df = clean_inspection_data(load_csv(inspection_path))

    sensor_kpis = compute_sensor_kpis(sensor_df)
    inspection_kpis = compute_inspection_kpis(inspection_df)
    machine_summary = build_machine_summary(sensor_kpis, inspection_kpis)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    machine_summary.to_csv(output_path, index=False)

    print("Sensor KPIs:")
    print(sensor_kpis)
    print()
    print("Inspection KPIs:")
    print(inspection_kpis)
    print()
    print("Machine summary:")
    print(machine_summary)
    print()
    print(f"Saved report to: {output_path}")