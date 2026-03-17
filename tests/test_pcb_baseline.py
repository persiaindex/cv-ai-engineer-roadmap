from pathlib import Path
import json
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_pcb_baseline_creates_report() -> None:
    script_path = PROJECT_ROOT / "scripts" / "run_pcb_baseline.py"
    result = subprocess.run([sys.executable, str(script_path)], check=True, capture_output=True, text=True)

    report_path = PROJECT_ROOT / "projects" / "pcb_defect_baseline" / "output" / "baseline_report.json"
    assert report_path.exists()

    with report_path.open("r", encoding="utf-8") as file:
        report = json.load(file)

    assert report["image_count"] >= 1
    assert "records" in report
    assert len(report["records"]) >= 1
    assert "Report created" in result.stdout