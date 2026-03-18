from pathlib import Path
import json
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_detection_project_creates_report() -> None:
    script_path = PROJECT_ROOT / "scripts" / "run_detection_project.py"
    result = subprocess.run([sys.executable, str(script_path)], check=True, capture_output=True, text=True)

    report_path = PROJECT_ROOT / "projects" / "inspection_detection_baseline" / "output" / "detection_project_report.json"
    assert report_path.exists()

    with report_path.open("r", encoding="utf-8") as file:
        report = json.load(file)

    assert report["project_name"] == "inspection_detection_baseline"
    assert "detection_count" in report
    assert "linked_reports" in report
    assert "Project report created" in result.stdout