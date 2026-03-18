from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.detector_inference import draw_detections, run_detection, save_detection_json



def main() -> None:
    image_path = PROJECT_ROOT / "data" / "detection" / "input" / "sample_scene.jpg"
    output_image = PROJECT_ROOT / "data" / "detection" / "output" / "sample_scene_detected.jpg"
    output_json = PROJECT_ROOT / "data" / "detection" / "output" / "sample_scene_detections.json"

    detections = run_detection(image_path, score_threshold=0.4)
    draw_detections(image_path, detections, output_image)
    save_detection_json(output_json, image_path, detections)

    print(f"Input image: {image_path}")
    print(f"Detections kept: {len(detections)}")
    print(f"Annotated output: {output_image}")
    print(f"JSON report: {output_json}")


if __name__ == "__main__":
    main()