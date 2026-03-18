from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.onnx_export import benchmark_and_save_report



def test_benchmark_and_save_report_creates_outputs() -> None:
    image_dir = PROJECT_ROOT / "data" / "datasets" / "inspection_cls" / "val" / "defect"
    image_files = list(image_dir.glob("*.jpg")) + list(image_dir.glob("*.png"))
    assert image_files, "No validation image found for ONNX benchmark test."

    sample_image = image_files[0]
    checkpoint_path = PROJECT_ROOT / "artifacts" / "transfer_resnet18.pt"
    onnx_path = PROJECT_ROOT / "artifacts" / "onnx_test" / "transfer_resnet18_test.onnx"
    report_path = PROJECT_ROOT / "artifacts" / "onnx_test" / "onnx_benchmark_report_test.json"

    report = benchmark_and_save_report(sample_image, checkpoint_path, onnx_path, report_path)

    assert onnx_path.exists()
    assert report_path.exists()
    assert "same_prediction" in report

    with report_path.open("r", encoding="utf-8") as file:
        saved_report = json.load(file)

    assert "pytorch_time_seconds" in saved_report
    assert "onnx_time_seconds" in saved_report