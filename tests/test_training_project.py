from pathlib import Path
import json
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_training_project_creates_report() -> None:
    script_path = PROJECT_ROOT / "scripts" / "run_training_project.py"
    result = subprocess.run([sys.executable, str(script_path)], check=True, capture_output=True, text=True)

    report_path = PROJECT_ROOT / "projects" / "inspection_training_baseline" / "output" / "training_project_report.json"
    assert report_path.exists()

    with report_path.open("r", encoding="utf-8") as file:
        report = json.load(file)

    assert report["project_name"] == "inspection_training_baseline"
    assert len(report["class_names"]) == 2
    assert report["sample_count"] >= 1
    assert "Project report created" in result.stdout