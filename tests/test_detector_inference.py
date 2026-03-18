from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.detector_inference import save_detection_json



def test_save_detection_json_creates_file() -> None:
    output_path = PROJECT_ROOT / "artifacts" / "detection_test" / "detections.json"
    image_path = PROJECT_ROOT / "data" / "detection" / "input" / "sample_scene.jpg"
    detections = [
        {
            "label_id": 44,
            "label_name": "bottle",
            "score": 0.9,
            "box": [10.0, 10.0, 50.0, 80.0],
            "image_size": [320, 240],
        }
    ]

    save_detection_json(output_path, image_path, detections)
    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        report = json.load(file)

    assert report["detection_count"] == 1
    assert report["detections"][0]["label_name"] == "bottle"