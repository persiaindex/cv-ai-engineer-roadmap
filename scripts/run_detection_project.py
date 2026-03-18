from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]



def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



def main() -> None:
    config_path = PROJECT_ROOT / "configs" / "detection" / "detection_project.json"
    config = load_json(config_path)

    input_image = PROJECT_ROOT / config["input_image"]
    annotated_output = PROJECT_ROOT / config["annotated_output"]
    detection_json = PROJECT_ROOT / config["detection_json"]
    metrics_report_path = PROJECT_ROOT / config["metrics_report"]
    strategy_report_path = PROJECT_ROOT / config["strategy_report"]
    onnx_report_path = PROJECT_ROOT / config["onnx_report"]
    project_report_path = PROJECT_ROOT / config["project_report"]

    detection_report = load_json(detection_json)
    metrics_report = load_json(metrics_report_path)
    strategy_report = load_json(strategy_report_path)
    onnx_report = load_json(onnx_report_path)

    project_report = {
        "project_name": "inspection_detection_baseline",
        "input_image": str(input_image),
        "annotated_output_exists": annotated_output.exists(),
        "detection_count": detection_report["detection_count"],
        "boxes_after_nms": metrics_report["boxes_after_nms"],
        "precision": metrics_report["precision"],
        "recall": metrics_report["recall"],
        "ready_for_tiny_finetune": strategy_report["structure_report"]["ready_for_tiny_finetune"],
        "onnx_same_prediction": onnx_report["same_prediction"],
        "linked_reports": {
            "detection_json": str(detection_json),
            "metrics_report": str(metrics_report_path),
            "strategy_report": str(strategy_report_path),
            "onnx_report": str(onnx_report_path),
        },
    }

    project_report_path.parent.mkdir(parents=True, exist_ok=True)
    with project_report_path.open("w", encoding="utf-8") as file:
        json.dump(project_report, file, indent=2)

    print(f"Project report created: {project_report_path}")
    print(f"Detection count: {project_report['detection_count']}")
    print(f"Boxes after NMS: {project_report['boxes_after_nms']}")
    print(f"Ready for tiny fine-tune: {project_report['ready_for_tiny_finetune']}")
    print(f"ONNX same prediction: {project_report['onnx_same_prediction']}")


if __name__ == "__main__":
    main()