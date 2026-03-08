from pathlib import Path
import sys

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from analytics.cleaners import clean_inspection_data, clean_sensor_data
from analytics.metrics import (
    build_machine_summary,
    compute_inspection_kpis,
    compute_sensor_kpis,
)


def test_clean_sensor_data_fills_missing_values() -> None:
    df = pd.DataFrame(
        {
            "machine_id": ["M-1", "M-1", "M-1"],
            "timestamp": ["2026-03-01 08:00:00", "2026-03-01 12:00:00", "2026-03-01 16:00:00"],
            "fill_level": [10.0, None, 30.0],
            "temperature": [60.0, 61.0, 62.0],
            "vibration": [0.2, 0.3, 0.4],
        }
    )

    cleaned = clean_sensor_data(df)
    assert cleaned["fill_level"].isna().sum() == 0


def test_clean_inspection_data_normalizes_status() -> None:
    df = pd.DataFrame(
        {
            "inspection_id": ["I-1"],
            "machine_id": ["M-1"],
            "timestamp": ["2026-03-01 09:00:00"],
            "defect_score": [0.8],
            "status": [" Defective "],
        }
    )

    cleaned = clean_inspection_data(df)
    assert cleaned.loc[0, "status"] == "defective"


def test_compute_sensor_kpis_returns_expected_columns() -> None:
    df = pd.DataFrame(
        {
            "machine_id": ["M-1", "M-1"],
            "timestamp": pd.to_datetime(["2026-03-01 08:00:00", "2026-03-01 12:00:00"]),
            "fill_level": [10.0, 20.0],
            "temperature": [60.0, 70.0],
            "vibration": [0.2, 0.5],
        }
    )

    summary = compute_sensor_kpis(df)
    assert "avg_fill_level" in summary.columns
    assert summary.loc[0, "max_vibration"] == 0.5


def test_build_machine_summary_creates_attention_flag() -> None:
    sensor_kpis = pd.DataFrame(
        {
            "machine_id": ["M-1"],
            "avg_fill_level": [15.0],
            "min_fill_level": [15.0],
            "avg_temperature": [70.0],
            "max_vibration": [0.5],
        }
    )

    inspection_kpis = pd.DataFrame(
        {
            "machine_id": ["M-1"],
            "inspection_count": [2],
            "avg_defect_score": [0.8],
            "defective_count": [1],
        }
    )

    summary = build_machine_summary(sensor_kpis, inspection_kpis)
    assert summary.loc[0, "needs_attention"] == True